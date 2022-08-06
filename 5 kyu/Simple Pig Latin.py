# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
#
# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word. Leave punctuation marks untouched.

text = input('Input text: ')
result = ''

for word in text.split():
    if word.isalpha():
        result += word[1:] + word[0] + 'ay'
    else:
        result += word
    result += ' '

result = result[:-1]

print(result)
