# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

lst = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]

result = []
number_zeros = 0
for item in lst:
    if item != 0:
        result.append(item)
    else:
        number_zeros += 1

for _ in range(number_zeros):
    result.append(0)

print(lst)
print(result)
