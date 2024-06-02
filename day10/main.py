"""
files
"""
fp = open("data.txt", mode='r')

# result = fp.read()
# for line in fp:
#     print(line.strip())

# print(result)
lines = fp.readlines()

out = [x.strip() for x in lines]

print(out)

fp.close()

res = []

for val in out:
    res.append(
        val + " - nhan"
    )

print(res)
fw = open("result.txt", mode='w')

for x in res:
    fw.write(x + '\n')

fw.close()
