'''
1. values
- int: 1, -1, 0, 100, ..
- float: 1.45, -0.5, 3.14, ...
- str: 'abcd', "def13245365", """line1""", \'\'\'line2\'\'\'
- bool: True/False
- complex: z = a + bj (j^2 = -1)

2. variables

3. input() built in function -> str

4. int() -> int
   float() -> float
   str() -> str
   bool() -> boolean (True/False) - Falsy: 0, 0.0, None, ''
'''
# type() built in function - type checking
# print(type(100))
# print(type('xy'))
# print(type(True), type(False))
# print(type(1234+1234j))

# x - variable
x = 100
print(x)

x = 1
print(x)

x = True
print(x)

##
name = input("Enter your full name: ")  # -> str

print(type(name))
print(name)

##
x = int(input('> '))

print(type(x))
print(x + 100)

##
a = float(input('enter your float: '))
print(type(a))
print(a/0.5)

##
a = int(input("enter your number: "))  # -> str
print("vnd =", a*24725)

##
name = "Vo Quang Nhan"
# I'm Vo Quang Nhan!
print("I'm " + name + '!')
print(f"I'm {name}!")
print("I'm {}!".format(name))

##
# online judge - OJ
