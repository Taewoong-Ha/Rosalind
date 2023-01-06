import re
import time
import sys

start = time.time()  # 시작 시간 저장

def Freq_Words(text, k , t):
    kmer_count = {} # 딕셔너리 형태로 kmer 별로 count를 하겠다.
    for i in range(len(text) - k + 1):
        kmer = text[i : i + k] # text에서 i번째 kmer
        if kmer not in kmer_count: # kmer_count에 kmer가 없으면 kmer를 key로 지정하고 value에 1을 추가
            kmer_count[kmer] = 1 
        else:                      # kmer_count에 kmer가 있으면 kmer를 key로 하는 value에 1을 더하기
            kmer_count[kmer] += 1
    
    maxcount = max(kmer_count.values()) #  kmer_count의 values 중에 최대 값
    if maxcount < t:                    # 최대값이 t보다 작으면 빈 결과를 반환
        return []
    else:                               # 최대값이 t보다 작지 않으면. count ==  t인 kmer를 반환
        aa = []
        for kmer, count in kmer_count.items():
            if count == t:
                aa.append(kmer)
        return aa
    
def FindClump(genome, k, L, t):
    clump = set()                        # 중복을 허용하지 않는 빈 배열 만들기
    for i in range(len(genome) - L + 1):
        sub = genome[i : i + L]          # 윈도우 사이즈에 맞는 sub_genome 생성
        sub_kmer = Freq_Words(sub, k, t) # t번 등장하는 sub_kmer 만들기
        for kmer in sub_kmer:
            clump.add(kmer)
    return clump

    
genome = input()
k = int(input())
L = int(input())
t = int(input())

print(" ".join(FindClump(genome, k, L, t)))


print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간



# if __name__ == "__main__":
#     '''
#     Given: A string Genome, and integers k, L, and t.
#     Return: All distinct k-mers forming (L, t)-clumps in Genome.
#     '''
#     input_lines = sys.stdin.read().splitlines()
#     Genome = input_lines[0]
#     k, L, t = [int(x) for x in input_lines[1].split()]

#     print(" ".join(find_clumping_kmers(Genome, k, L, t)))
