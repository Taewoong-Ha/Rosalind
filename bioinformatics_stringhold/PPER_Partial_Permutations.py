# Partial permutation 
# 참고: https://m.blog.naver.com/pomaths/222905145077

'''
Given: Positive integers n and k such that 100≥n>0 and 10≥k>0
Return: The total number of partial permutations P(n,k) modulo 1,000,000.
n = 21, k = 7
result = 51200
'''
import math # factorial 사용

def Partial_Permutation(n, k):
    f = math.factorial
    n_fac = f(n) # 분자
    k_fac = f(n-k) # 분모
    modulo = (n_fac / k_fac) % 1000000 # modulo는 나머지를 의미
    return round(modulo)


if __name__ == "__main__":
    n = int(input())
    k = int(input())

    print(Partial_Permutation(n,k))


