import itertools
from Bio.Seq import Seq

def Hamming_Distance(p, q):
    ham_dis = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            ham_dis += 1
    return ham_dis


# dna.reverse_complement()

def d_mismatch_most_freq_kmer(text, k, d):
    
    freq_kmer = {}
    kmers = list(map(''.join, itertools.product('ACGT', repeat=k)))
    
    for kmer in kmers:
        freq_kmer[kmer] = 0
        for i in range(len(text) - k + 1):
            sub = text[i : i + k]
            if Hamming_Distance(kmer, sub) <= d: #
                freq_kmer[kmer] += 1
            # elif Hamming_Distance(Seq(kmer).reverse_complement(), sub) <= d:
            #     freq_kmer[kmer] += 1
                
        for i in range(len(text) - k + 1):
            sub = text[i : i + k]
            if Hamming_Distance(Seq(kmer).reverse_complement(), sub) <= d:
                freq_kmer[kmer] += 1


    most_kmer = [ key for key, val in freq_kmer.items() if max(freq_kmer.values()) == val]
            
    return  most_kmer

if __name__ == "__main__":
    with open("C:/Users/user/Downloads/rosalind_ba1j (1).txt", "r") as f:
        lines = f.readlines()
        text = lines[0].strip('\n')
        dd = lines[1].strip('\n').split(' ')
        k = int(dd[0])
        d = int(dd[1])
 
#     print(d_mismatch_most_freq_kmer(text, k, d))
    print(" ".join(map(str, d_mismatch_most_freq_kmer(text, k, d))))
