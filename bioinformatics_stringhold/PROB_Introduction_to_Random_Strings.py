'''Introduction to Random Strings
주어진 것 
GC-content가 x면 probability는 x/2
AT-content는 1-x이고 probability는 (1-x) / 2

A[K]는 array A의 k번째 배열
String은 고정된 확률의 symbol frequent를 기반으로 구축됨

input
s =  DNA string
array A = 20개 숫자 (0~1사이 random)

output
array A의 k번째 숫자를 가지고 s의 확률 추정 using log10
'''

# 1. at와 gc의 count에 대해 계산
def allele_count(S):
    at = 0
    gc = 0
    for s in S:
        if s == "A" or s == "T":
            at += 1
        else:
            gc += 1
    return at, gc
  
# 2. allele count와 A[k] = GC-content를 이용해서 log(확률) 추정
def logarithm_string(S, A):
    at = allele_count(S)[0]
    gc = allele_count(S)[1]
    pp_at = 0
    pp_gc = 0
    B = []
    for a in A:
        a = float(a)
        pp_at = (( 1 - a ) / 2)**at
        pp_gc = (a / 2)**gc
        log = math.log10
        B.append(round( log(pp_at) + log(pp_gc), 3))
    return B
        
    
with open("/Users/hataewoong/Downloads/rosalind_prob.txt", "r") as f:
  lines = f.readlines()
  S = str(lines[0].split())
  A = lines[1].split()
                
  print(" ".join(map(str,logarithm_string(S, A))))
