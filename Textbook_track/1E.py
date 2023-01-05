import re
import time

start = time.time()  # 시작 시간 저장

def Freq_Words(text, k , t):
    kmer_count = {}
    for i in range(len(text) - k + 1):
        kmer = text[i : i + k]
        if kmer not in kmer_count:
            kmer_count[kmer] = 1
        else:
            kmer_count[kmer] += 1
    
    maxcount = max(kmer_count.values())
    if maxcount < t:
        return []
    else:
        aa = []
        for kmer, count in kmer_count.items():
            if count == t:
                aa.append(kmer)
        return aa
    
def FindClump(genome, k, L, t):
    clump = set() # 중복을 허용하지 않는 빈 배열 만들기
    for i in range(len(genome) - L + 1):
        sub = genome[i : i + L] # 윈도우 사이즈에 맞는 sub_genome 생성
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
