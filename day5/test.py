n = int(input())
set_n = set()

for _ in range(n):
    country = input()
    set_n.add(country)
    print(set_n)

print(len(set_n))
