sentence = input('Input string: ')

result_list = []
for word in sentence.split():
    if len(word) > 4:
        result_list.append(word[::-1])
    else:
        result_list.append(word)

result = ' '.join(result_list)
print(result)
