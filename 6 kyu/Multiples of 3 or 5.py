n = int(input('Input integer number: '))

result = 0

for i in range(3, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)
