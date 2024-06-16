# """
# set
# dict
# """
# ## - set
# set_a = {1, 2, 3, 4}
# print(type(set_a))
#
# set_b = set()  # empty set
# print(len(set_b))
#
# set_a.add(1)
# set_a.add(1)
#
# print(set_a)
#
# # set_a.remove(1000)
# set_a.discard(1000)
#
# val = set_a.pop()
# print(val)
# print(set_a)
#
# ## - set 2
# a = {1, 2, 3, 4}
# b = {3, 5, 4, 7}
# # {3, 4}
# both = a.intersection(b)
# print(both)
# print(a & b)
#
# # {1, 2}
# result = a.difference(b)
# print(result)
# print(a - b)
#
# # {5, 7}
# print(b.difference(a))
# print(b - a)
#
# # {1, 2, 5, 7}
# print(a.symmetric_difference(b))
# print(a ^ b)
#
# # {1, 2, 3, 4, 5, 7}
# print(a.union(b))
# print(a | b)
#
# ## - dict
# d = {
#     'a': 1,
#     'b': 123,
#     'c': 1000
# }
#
# print(type(d))
# print(d)
#
# print(d['a'])
# print(d['c'])
#
# d['a'] = 10000
# print(d)
# d['b'] = ""
# print(d)
#
# print(d['a'])
# print(d.get('a'))
#
# # print(d.get('abc', 1))
# # print(d['abc'])
#
# print(d.pop('a'))
# print(d)
#
# del d['b']
# print(d)
#
# print(d.popitem())
# print(d)
#
# d = {1: [1, 2, 3], 10: (4, 5, 6)}
# print(list(d.values()))
# print(list(d.items()))
# print(list(d))
#
# d.update({0: -1, 9: -2})
# d[1000] = 123
#
# print(d)
# ##
# a = [1, 2, 3, 1, 1]
# """
# {1: 3,
# 2: 1,
# 3: 1,}
# """
#
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
    leap = False

    return leap

year = int(input(':'))
print(is_leap(year))