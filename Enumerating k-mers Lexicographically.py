from itertools import product

string = ["A", "B", "C", "D", "E", "F", "G", "H"]
length = 3

for i in product(string, repeat = length):
    # print(i)
    k = ""
    for j in i:
        k = k + j
        if len(k) < length:
            pass
        else:
            # print(len(k))
            print(k)

