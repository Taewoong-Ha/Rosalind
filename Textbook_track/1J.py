'''
Frequent Words with Mismatches and Reverse Complements Problem
Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.

Given: A DNA string Text as well as integers k and d.
Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern_rev_com) over all possible k-mers.

Sample Dataset: 
ACGTTGCATGTCGCATGATGCATGAGAGCT 
4 1
Sample output
ATGT ACAT
'''
import itertools
from Bio.Seq import Seq # biopython package로 revere complement seq을 한번에 계산해줌 굳

def Hamming_Distance(p, q): # Hamming distance 계산 -  두 string사이의 mismatch의 개수
    ham_dis = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            ham_dis += 1
    return ham_dis


# dna.reverse_complement()

def d_mismatch_most_freq_kmer(text, k, d): # 최대 d개의 mismatch를 허용하는 가장 빈번한 k-mer
    # 오류 출력
    if not k <= 12 and k >= 1: 
        raise ValueError("motif_length must be between 0 and 12. {} was passed.".format(k))
    if not d <= 3 and d >= 1:
        raise ValueError("max_mismatch must be between 0 and 3. {} was passed.".format(d))
   
    freq_kmer = {} #kmer에 대한 빈도수 dict
    kmers = list(map(''.join, itertools.product('ACGT', repeat=k))) # ACGT로 길이가 k인 중복순열
        
    for kmer in kmers: 
        freq_kmer[kmer] = 0 # 4**k의 개수를 갖는 kmer에 대해 kmer를 key로 지정 후 값은 0
        for i in range(len(text) - k + 1): # 길이만큼 포문 돌고
            sub = text[i : i + k] # text에서 kmer를 추출
            if Hamming_Distance(kmer, sub) <= d: # kmer와 sub사이의 ham_dis가 d보다 작거나 같으면 kmer에 1을 더함
                freq_kmer[kmer] += 1 

            if Hamming_Distance(Seq(kmer).reverse_complement(), sub) <= d: # kmer의 reverse complement와 sub사이의 ham_dis가 d보다 작거나 같으면 kmer에 1을 더함
                freq_kmer[kmer] += 1

    most_kmer = [ key for key, val in freq_kmer.items() if max(freq_kmer.values()) == val] # 가장 빈번한 kmer 출력
            
    return  most_kmer

if __name__ == "__main__":
    with open("C:/Users/user/Downloads/rosalind_ba1j.txt", "r") as f:
        lines = f.readlines()
        text = lines[0].strip('\n')
        dd = lines[1].strip('\n').split(' ')
        k = int(dd[0])
        d = int(dd[1])
 
    print(" ".join(map(str, d_mismatch_most_freq_kmer(text, k, d))))
