# Operators
"""
1. +, -, *, /, //, %, **
2. >, <, >=, <=, ==, != => True/False
3. not > and > or
4. +=, -=, *=, ...
"""
##
print(12 + 13)
print(12 - 13)
print(12 * 13)
print(12 / 13)  # float
print(12 // 13)  # int
print(12 % 5)  # int
print(2 ** 3)

##
print(1 > 2)  # False
print(1 < 2)  # True
print(1 != 2)  # True
print(5.0 == 5)  # True
print('a' >= 'b')
print('a' <= 'b')

##
print(1 > 2 and 3 > 2)  # False and True = False
print(1 < 2 and 3 > 2)  # True and True = True
print(1 > 2 and 3 < 2)  # False and False = False

print(1 > 2 or 3 > 2)  # False or True = True
print(1 < 2 or 3 > 2)  # True or True = True
print(1 > 2 or 3 < 2)  # False or False = False

print(not True)  # False
print(not False)  # True

##
user_name = input('> ')
print(user_name or "Nhan")

##
x = 2
# x = x ** 2
x **= 2

print(x)

##

