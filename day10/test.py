with open("googleplaystore.csv", mode='r', encoding="utf8") as csv_file:
    for line in csv_file:
        values = line.strip().split(',')
        print(values)

