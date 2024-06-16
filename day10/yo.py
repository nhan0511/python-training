n = int(input("input your number: "))
    if n % 2 == 0:
        print("Weird")
    for n in range(2, 5):
        print("Not Weird")
    for n in range(6, 20):
        print("Weird")
    if n % 2 == 1 and n > 20:
        print("Not Weird")
    else:
        print("Error")
