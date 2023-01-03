## Compute the Number of Times a Pattern Appears in a Text 
## Sample Dataset
## GCGCG
## GCG
## Sample Output: 2


def patterncount(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern) +1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count

text = input()
pattern = input()

patterncount(text,pattern)

