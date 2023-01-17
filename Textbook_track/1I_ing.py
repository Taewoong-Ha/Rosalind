def Hamming_Distance(p, q):
    ham_dis = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            ham_dis += 1
    return ham_dis

def d_mismatch_most_freq_kmer(text, k, d):
    most_kmer = {}
    for i in range(len(text) - k + 1):
        i_kmer = text[i : i + k] 
        for j in range(len(text) - k + 1):
            j_kmer = text[j : j + k] 
            if Hamming_Distance(i_kmer,j_kmer) == d:
                if j_kmer not in most_kmer:
                    most_kmer[j_kmer] = 1
                else:
                    most_kmer[j_kmer] += 1
    lst = [key for key,val in most_kmer.items() if max(most_kmer.values()) == val]
    return lst


text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

d_mismatch_most_freq_kmer(text, k, d)


################################################################
# 아래 코드의 문제 1. 너무 많은 포문을 돌려서 비효율적임 특히 d_mismatch_most_freq_kmer의 두번째 포문..
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

def d_mismatch_most_freq_kmer(text, k, d):
    kmer = {}
    atgc = ["A","T","G","C"]
    for i in print_itertools(list(itertools.product(atgc, repeat = k))):
        kmer[i] = 0
        
    for i in range(len(text) - k + 1):
        sub = text[i:i+k]
        for key in kmer.keys():
            if Hamming_Distance(sub, key) == d:
                kmer[key] += 1
    lst = [key for key,val in kmer.items() if max(kmer.values()) == val]
    real = []
    for i in lst:
        if i in text:
            real.append(i)
    return real

### 그래서 수정한게 아래 # 근데 여기의 문제점은 없는 key에 해당하는 것은 찾아주지 않는다 -> text안의 kmer는 다 맞추는데 text에 없는 kmer는 뽑아주지않은...

def d_mismatch_most_freq_kmer(text, k, d):
    kmers = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        kmers[kmer] = 0
        
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        for key in kmers.keys():
            if Hamming_Distance(kmer, key) == d:
                kmers[key] += 1
#     lst = [key for key,val in kmers.items() if max(kmers.values()) == val]
    return kmers

text = "AGGT"
k = 2
d = 1
# GATG ATGC ATGT
d_mismatch_most_freq_kmer(text, k, d)
text = "AGGT"
k = 2
d = 1
# GATG ATGC ATGT
d_mismatch_most_freq_kmer(text, k, d)
