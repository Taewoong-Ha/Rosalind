import itertools
import pandas as pd


def dif_minus_change(lst1, lst2):
    ccc = []
    ccc = list(set(lst1) - set(lst2))
    for i in lst2:
        ccc.append(-i)
    return ccc

n = 5
nums = list(range(1,n+1))

print("\n")
aa = []

a = []
for i in range(n+1): # i = 0,1,2,3
    if i == 0:
        for i in list(itertools.permutations (nums,n)):
        # print(" ".join(map(str, i)))
            aa.append(" ".join(map(str, i)))
    else:
        for j in  list(itertools.combinations(nums,i)):
            j = list(j)
            nums = dif_minus_change(nums, j)            
            # pass
            for k in list(itertools.permutations (nums,n)):
                aa.append(" ".join(map(str, k)))
            nums = list(range(1,n+1))    

# print(aa)
print(len(aa))

for i in aa:
    print(i)

