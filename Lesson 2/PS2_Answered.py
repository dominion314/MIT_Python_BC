'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''

s = 'azcbobobegghakl'
countBob = 0

for char in s:
    list = countBob.split('')
    if char == 'bob':
        countBob += 1
print('Number of times bob occurs is: ' + str(countBob))