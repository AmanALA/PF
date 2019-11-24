# Code by Infiltrat8r

var = lambda str: True if str == str[::-1] else False
result = var(input('Enter string: '))
print('It is {} that your string is a palindrome'.format(result))


