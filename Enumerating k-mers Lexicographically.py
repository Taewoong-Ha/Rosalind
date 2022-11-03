from itertools import product
# 불러오기
f = open('C:/Users/user/Downloads/rosalind_lexf.txt','r')
# 공백으로 분리해서 리스트 형태로 저장
lines = f.read().split()
string = lines[:len(lines)-1]
length = int(lines[-1])


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



