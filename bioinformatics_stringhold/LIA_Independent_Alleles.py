# 주어진 단서
'''
1. AaBb 확률 = 0.25
2. AaBb가 나오지 않을 확률 0.75
3. k-th generation
4. 1세대가 갈수록 2배씩 인구 증가 Total_off = 2**k
5. 적어도 N만큼 AaBb가 나올 확률 N <= 2**k
'''
# 문제 해결 방법
'''
1. bionom or factorial 사용 
    참고: https://angeloyeo.github.io/2021/04/23/binomial_distribution.html
2. 1 - N보다 적게 나타날 확률 or N~2**k사이의 확률 모두 더하기
'''

'''나의 선택 factorial & N보다 적게 나타날 확률
'''
import math. # factorial을 쓰기위해 math 모듈 import
from scipy.special import binom # 이항분포인 binom을 사용하기 위해 scipy 모듈 import

def nCr(n, k):
    f = math.factorial
    return f(n) / (f(k) * f(n-k))

def Probability(N, k):
    pp = 0
    AaBb_p = 0.25
    total = 2**k
    for n in range(N):
        kth_p = nCr(total, n) * AaBb_p**n * (1-AaBb_p)**(total -n)
        pp += kth_p
    return round(1 - pp,3)

if __name__ == "__main__":
    k = int(input())
    N = int(input())

    print(Probability(N,k))
