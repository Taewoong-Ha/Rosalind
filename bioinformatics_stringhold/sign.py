import itertools  # permutations & combinations 사용을 위함
import pandas as pd


def dif_minus_change(lst1, lst2): # 교집합에 해당하는 것을 -로 변환하기 위함
    ccc = []
    ccc = list(set(lst1) - set(lst2))
    for i in lst2:
        ccc.append(-i)
    return ccc

n = 5 # 주어진 수 
nums = list(range(1,n+1)) # 1~n까지의 list

print("\n")
aa = []

for i in range(n+1): # i = 0,1,2,3
    # 일단 모든 부호가 양수일 경우를 대상으로 permutation
    if i == 0: #
        for i in list(itertools.permutations (nums,n)):
        # print(" ".join(map(str, i)))
            aa.append(" ".join(map(str, i)))
    # 그리고 조합에 - 부호를 붙임
    # i = 1은 1개가 -부호
    # i = 2는 2개가 -
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

