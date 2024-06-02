print(1)

try:
    print(1/2)
except Exception as e:
    print(e)
except ZeroDivisionError as e:
    print("error")
else:
    print("success")
finally:
    print("always run")

print(2)

a = input("input: ")
b = input("input: ")
T = a/b

