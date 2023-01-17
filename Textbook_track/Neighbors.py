
''' text에서 최대 해밍거리가 d인 kmer만 고려해 보자.
조어진 kmer에서 Neighbors(pattern, d)는 pattern과 유사한 모든 kmer의 집합이다. 
예를들어
Neighbors(ACG,1)은 다음 열개의 3-mer로 나타낼 수 있다.
AAG ATG AGG ACA ACT ACG ACC TCG GCG CCG
'''
import itertools

def print_itertools(itertool):
    dd = []
    for i in itertool:
        output = ""
        for j in i:
            j = str(j)
            output = output + j
        dd.append(output)
    return dd

def Hamming_Distance(p, q):
    ham_dis = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            ham_dis += 1
    return ham_dis


def Neighbors(pattern, d):
    neighbors = []
    pattern = pattern
    atgc = ["A","T","G","C"]
    for i in print_itertools(list(itertools.product(atgc, repeat = len(pattern)))):
        if Hamming_Distance(pattern, i) <= 1:
            neighbors.append(i)
    return neighbors

pattern = "ACG"
d = 1
print(" ".join(map(str, Neighbors(pattern, d))))
