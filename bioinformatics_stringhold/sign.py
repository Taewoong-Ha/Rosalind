import itertools
import pandas as pd

n = 3
nums = list(range(1,n+1))

print("\n")
aa = []
for i in list(itertools.permutations (nums,n)):
    # print(" ".join(map(str, i)))
    aa.append(" ".join(map(str, i)))

print(aa)

a = []
for i in range(n+1): # i = 0,1,2,3
    # print(list(itertools.combinations(nums,i)))
    if i == 0:
        for i in list(itertools.permutations (nums,n)):
        # print(" ".join(map(str, i)))
            aa.append(" ".join(map(str, i)))
    else:
        for j in  list(itertools.combinations(nums,i)):
            j = list(j); nums = list(range(1,n+1))
            # nums.replace(j, -j) ######## 이 부분만 바꾸면 됨
            print(j)
            pass
            for i in list(itertools.permutations (nums,n)):
                # print(" ".join(map(str, i)))
                aa.append(" ".join(map(str, i)))
