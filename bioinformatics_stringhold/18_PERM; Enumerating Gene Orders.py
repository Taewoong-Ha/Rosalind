## Problem
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.
Given: A positive integer n≤7.
Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

## Sample Dataset
3

## solved code
import itertools

f = open('C:/Users/user/Downloads/rosalind_perm.txt', 'r')
lines = f.readlines()
for line in lines:
    line = line.split("\n")[0]
    sample_data = int(line)
# print(sample_data)

integral  = []

for i in range(sample_data):
    integral.append(i+1)
    
# print(integral)
nCr = itertools.permutations(integral, sample_data)
a = list(nCr)
print(len(a))

for i in a:
    output = ""
    for j in i:
        j = str(j)
        output = output + j + " "
    print(output)
