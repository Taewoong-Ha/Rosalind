'''
Find All Approximate Occurrences of a Pattern in a String
We say that a k-mer Pattern appears as a substring of Text with at most d mismatches 
if there is some k-mer substring Pattern' of Text having d or fewer mismatches with Pattern,
i.e., HammingDistance(Pattern, Pattern') ≤ d. 
Our observation that a DnaA box may appear with slight variations leads to the following generalization of the Pattern Matching Problem.
'''

def Hamming_Distance(p, q):
    ham_dis = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            ham_dis += 1
    return ham_dis

def Approximate_Pattern_Count(text, pattern, d):
    approx_count = []
    for i in range(len(text) - len(pattern) + 1):
        q = text[i : i + len(pattern)]
        if Hamming_Distance(pattern, q) <= d:
            approx_count.append(i)
    return approx_count
        
if __name__ == "__main__":
  '''
  Given: Strings Pattern and Text along with an integer d.
  Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
  '''
    with open("/Users/hataewoong/Downloads/rosalind_ba1h.txt", "r") as f:
        lines = f.readlines()
        d = int(lines[2].strip())
        
        if len(lines[0].strip()) > len(lines[1].strip()):
            text = lines[0].strip()
            pattern = lines[1].strip()
        else:
            pattern = lines[0].strip()
            text = lines[1].strip()
        
    print(" ".join(map(str, Approximate_Pattern_Count(text, pattern, d)) ) ) # 리스트를 [1, 2, 3] 형태가 아니 1 2 3 으로 출력
#     print(*Approximate_Pattern_Count(text, pattern, d)) #  리스트를 [1, 2, 3] 형태가 아니 1 2 3 으로 출력
