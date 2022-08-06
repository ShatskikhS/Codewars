# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

# Given an n x n array, return the array elements arranged
# from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

result = []
indent = 0
n = len(array)

while indent < n / 2:

    # top line
    for i in range(indent, n - indent):
        result.append(array[indent][i])

    # right line
    for j in range(indent + 1, n - indent):
        result.append(array[j][n-indent-1])

    # bottom line
    for i in range(n - indent - 2, indent - 1, -1):
        result.append(array[n - indent - 1][i])

    # Left line
    for j in range(n - indent - 2, indent, -1):
        result.append(array[j][indent])
    indent += 1

print(result)
