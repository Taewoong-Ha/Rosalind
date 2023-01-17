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


