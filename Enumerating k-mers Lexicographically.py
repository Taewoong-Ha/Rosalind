from itertools import product
# 불러오기
f = open('C:/Users/user/Downloads/rosalind_lexf.txt','r')
# 공백으로 분리해서 리스트 형태로 저장
lines = f.read().split()
string = lines[:len(lines)-1]
length = int(lines[-1])

# itertools의 product를 사용
# string을 length 만큼 반복
for i in product(string, repeat = length):
    # print(i) ('A', 'A', 'A') 이 형태
    # 문자열
    k = ""
    # AAA형태로 변환하기 위해서 또 다른 포문 사용
    for j in i:
        k = k + j
        if len(k) < length:
            pass
        else:
            # print(len(k))
            print(k)



