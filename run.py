import asyncio
from spiral_matrix import get_matrix

URL = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"

result = asyncio.run(get_matrix(URL))
print(result)