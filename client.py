import re
from typing import List

import aiohttp

_ROW_RE = re.compile(r"^\|(.+)\|$")

def _parse(text: str) -> List[List[int]]:
    rows = []
    for line in text.splitlines():
        line = line.strip()
        m = _ROW_RE.match(line)
        if not m:
            continue
        rows.append([int(c.strip()) for c in m.group(1).split("|")])
    if rows:
        n = len(rows)
        for row in rows:
            if len(row) != n:
                raise ValueError("Матрица не является квадратной")  
    return rows

def _spiral(matrix: List[List[int]]) -> List[int]:
    n = len(matrix)
    result = []
    top, bottom, left, right = 0, n - 1, 0, n - 1
    while top <= bottom and left <= right:
        for i in range(top, bottom + 1):
            result.append(matrix[i][left])
        left += 1
        for j in range(left, right + 1):
            result.append(matrix[bottom][j])
        bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][right])
            right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[top][j])
            top += 1
    return result

async def get_matrix(url: str) -> List[int]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
    return _spiral(_parse(text))