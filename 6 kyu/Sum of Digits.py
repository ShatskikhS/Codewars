# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

n = input('Input non-negative integer: ')

current_sum = sum([int(i) for i in n])

while current_sum > 9:
    current_sum = sum([int(i) for i in str(current_sum)])

print(current_sum)
