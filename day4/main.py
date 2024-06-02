## - 1
"""
list - []
"""
#          0  1  2  3  4   - index
#         -5 -4 -3 -2 -1
numbers = [1, 5, 6, 7, 8]  # - value

print(type(numbers))

print(numbers)

print(len(numbers))

numbers.append(100)

print(numbers)
print(numbers[0])
length = len(numbers)  # 6
print(numbers[length - 1])

print(numbers[-1])
print(numbers[-length])

print(numbers[2])

numbers.extend([1, 2, 3])
print(numbers)

last_value = numbers.pop()
print(last_value)
print(numbers)

numbers.remove(100)
print(numbers)

numbers.pop(0)
print(numbers)

del numbers[0]
print(numbers)

numbers.insert(0, 1000)
print(numbers)

numbers.insert(1, 100)
#   0   1   2  3  4  5  6
# 1000, 100 6, 7, 8, 1, 2
print(numbers)

numbers.append(1)
print(numbers)
# print(numbers.index(-1))

# print(numbers.count(-1))

numbers.reverse()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

copy_numbers = numbers.copy()

print(copy_numbers == numbers)
print(copy_numbers is numbers)

numbers.clear()
print(numbers)

## - 2
lst = [
    #    0   1    2
    [1, None, True],  # 0
    ['a', ..., False],  # 1
    [0, [3, 'l'], 100]  # 2
]

print(type(lst))
print(lst[2][2])
print(lst[2][1][1])
print(lst[0][2])
lst[1].append(10000)
print(lst)

lst[0][1] = 0.5
print(lst)

lst[1].extend([0] * 10)
print(lst)

##
s = "abcdef"
lst = list(s)

#   0    1    2    3    4    5    6
#  -7   -6   -5   -4   -3   -2   -1
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
lst.append('g')
lst.append('h')

print(lst)
print(lst[:3])
print(lst[4:])
print(lst[-3:])

print(lst[2:5])
print(lst[1:-1])

lst[1:-1] = []
print(lst)

##
lst = [0]

# += - extend
lst *= 2  # lst = lst * 2 = [0] * 2 = [0, 0]

print(lst)

##
x = 2
x *= 2  # x = x * 2
print(x)

##
# tuple
#       0  1  2
#      -3 -2 -1
tup1 = (1, 2, 3)
print(type(tup1))

length = len(tup1)
print(tup1[0])
print(tup1[-length])
print(tup1[-1])
print(tup1[length - 1])

tup2 = 1, 2, 3
print(type(tup2))

##
#   0  1  2  3
t = 1, 2, 3, 1
print(t.count(1))  # 2
print(t.index(1))  # 0

##
l =[1,2,3,4]
l.extend([69,69])
print("e",l)