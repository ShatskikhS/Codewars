seq = [1,1,2,-2,5,2,4,4,-1,-2,5]
#
# for numer in set(seq):
#     if seq.count(numer) % 2 == 1:
#         result = numer
#         break
#
# print(result)

print([number for number in set(seq) if seq.count(number) % 2 == 1][0])
