'''
Frequent Words with Mismatches Problem
Find the most frequent k-mers with mismatches in a string.
Given: A string Text as well as integers k and d.
Return: All most frequent k-mers with up to d mismatches in Text.

Sampel Dataset
ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1

Sample output
GATG ATGC ATGT
'''

import itertools

def Hamming_Distance(p, q):
    ham_dis = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            ham_dis += 1
    return ham_dis

def d_mismatch_most_freq_kmer(text, k, d):
    
    if not k <= 12 and k >= 1:
        raise ValueError("motif_length must be between 0 and 12. {} was passed.".format(k))
    if not d <= 3 and d >= 1:
        raise ValueError("max_mismatch must be between 0 and 3. {} was passed.".format(d))

    freq_kmer = {}
    kmers = list(map(''.join, itertools.product('ACGT', repeat=k)))
    
    for kmer in kmers:
        freq_kmer[kmer] = 0
        for i in range(len(text) - k + 1):
            sub = text[i : i + k]
            if hammingDistance(kmer, sub) <= d:
                freq_kmer[kmer] += 1
    most_kmer = [ key for key, val in freq_kmer.items() if max(freq_kmer.values()) == val]
            
    return most_kmer

if __name__ == "__main__":
#     text = input()
#     k = int(input())
#     d = int(input())

    
    text = "TGCGAAACCCTAACGGTGCGAAACGGAGTCCTCCTAACGGCGTGCCCTGCGAAACGGAGTCCTAACAATCACGTGCCCTGCGAAACTGCGAAACCGTGCCCTGCGAAACCCTAACGGGGAGTCCTAACAATCATGCGAAACGGAGTCCTGGAGTCCTAACAATCACGTGCCCTGCGAAACCCTAACGGTGCGAAACTGCGAAACCCTAACGGTGCGAAACGGAGTCCTTGCGAAACGGAGTCCTGGAGTCCTTGCGAAACAACAATCATGCGAAACGGAGTCCTCGTGCCCAACAATCAAACAATCATGCGAAACCCTAACGGGGAGTCCTGGAGTCCTCGTGCCCGGAGTCCTGGAGTCCTGGAGTCCTTGCGAAACAACAATCAGGAGTCCTCCTAACGGGGAGTCCTGGAGTCCTAACAATCAGGAGTCCTCGTGCCCCCTAACGGCGTGCCCGGAGTCCTTGCGAAACCGTGCCCTGCGAAACGGAGTCCTAACAATCAAACAATCAAACAATCAGGAGTCCTCCTAACGGCCTAACGGGGAGTCCTCGTGCCCGGAGTCCTCCTAACGGCCTAACGGAACAATCAAACAATCACCTAACGGCCTAACGGAACAATCAGGAGTCCTCCTAACGGCCTAACGGGGAGTCCTGGAGTCCTCCTAACGGTGCGAAACGGAGTCCTCGTGCCCCGTGCCCCGTGCCCTGCGAAACCCTAACGGGGAGTCCTCGTGCCCTGCGAAACCGTGCCCTGCGAAACTGCGAAACTGCGAAACAACAATCATGCGAAACAACAATCAAACAATCACGTGCCCAACAATCACCTAACGGGGAGTCCT"
    k = 5
    d = 2
    print(" ".join(map(str, d_mismatch_most_freq_kmer(text, k, d))))
