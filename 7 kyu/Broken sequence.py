# https://www.codewars.com/kata/5512e5662b34d88e44000060/train/python

sequence = input('input sequence: ')
seq = sequence.split()

for i in seq:
    if not i.isdigit():
        result = 1
        break
else:
    result = 0

if result == 0:
    for i in range(1, len(seq) + 1):
        for j in seq:
            if str(i) == j:
                break
        else:
            result = i
            break

print(result)
