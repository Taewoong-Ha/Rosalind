'''
The number of mismatches between strings p and q 
is called the Hamming distance 
between these strings and is denoted HammingDistance(p, q).

Hamming Distance Problem
Compute the Hamming distance between two DNA strings.
Given: Two DNA strings.
Return: An integer value representing the Hamming distance.
'''

import sys

def Hamming_Distance(p, q):
    ham_dis = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            ham_dis += 1
    return ham_dis

if __name__ == "__main__":
    '''
    Given: Two DNA strings.
    Return: An integer value representing the Hamming distance.
    '''
    with open("/Users/hataewoong/Downloads/rosalind_ba1g.txt", "r") as f:
        a = f.readlines()
        
    p = a[0].strip()
    q = a[1].strip()
    print(Hamming_Distance(p, q))
