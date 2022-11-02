# 힌트 1
# 2차원 배열을 통한 전수 조사
# print([0] * (len(Rosalind_1) + 1))
# print([[0]  for _ in range(len(Rosalind_2) + 1)]))

# 힌트 2
# 2차원 배열의 최대값 위치
# print(lcs)
# print(max(map(max, lcs)))
# print(np.argmax(lcs))
# print(np.argmax(lcs) // (len(Rosalind_1)+ 1))
# print(np.argmax(lcs) % (len(Rosalind_1) + 1))

# print(lcs[np.argmax(lcs) // (len(Rosalind_1)+ 1)][np.argmax(lcs) % (len(Rosalind_1) + 1)])



# seq 
Rosalind_1 = "ABCDEF"
Rosalind_2 = "GBCDFE"
Rosalind_3 = "ATACA"

# Result AC
# seq길이 + 1의 길이의 배열 생성
lcs = [[0] * (len(Rosalind_1) + 1) for _ in range(len(Rosalind_2) + 1)]
# 배열에 일치하면 값 넣고 아님 말고
for i in range(len(Rosalind_1) + 1):
    for j in range(len(Rosalind_2) +1 ):
        if i == 0 or j == 0:
            lcs[i][j] = 0
        elif Rosalind_1[i-1] == Rosalind_2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = 0
           
