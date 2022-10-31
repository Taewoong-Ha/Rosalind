# dataset 딕셔너리로 읽은 후 리스트로 전환
seq = {}
f = open('C:/Users/user/Downloads/rosalind_tran.txt','r')
lines = f.readlines()
for line in lines:
    if line.find('>') == 0:
        key = line.split('>')[1]
        key = key.split('\n')[0]
        seq[key] = '' 
    else:
        line = line.split('\n')[0]
        seq[key] += line
seq = list(seq.values())

first_seq = seq[0]
second_seq = seq[1]

# 0 값 할당
transition = 0 
transversion = 0

# 문제에 대한 값 지정
# else: \n pass 이 부분은 제거해도 되지만 그냥 넣음
for i in range(len(first_seq)):
    # print(i)
    if first_seq[i] == "A":
        if second_seq[i] == "G":
            transition += 1
        elif second_seq[i] == "C" or second_seq[i] == "T":
            transversion += 1
        else:
            pass
    if first_seq[i] == "T":
        if second_seq[i] == "C":
            transition += 1
        elif second_seq[i] == "A" or second_seq[i] == "G":
            transversion += 1
        else:
            pass
    if first_seq[i] == "G":
        if second_seq[i] == "A":
            transition += 1
        elif second_seq[i] == "C" or second_seq[i] == "T":
            transversion += 1
        else:
            pass
    if first_seq[i] == "C":
        if second_seq[i] == "T":
            transition += 1
        elif second_seq[i] == "A" or second_seq[i] == "G":
            transversion += 1
        else:
            pass
          
# print(transition)
# print(transversion)

# print(transition/transversion)
print(round(transition/transversion,11))
