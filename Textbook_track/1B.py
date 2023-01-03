
def patterncount(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern) +1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count


  
def FrequentWords(text, k):
    frequentspatterns = []
    count = []
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]
        count.append(patterncount(text, pattern))
    maxcount = max(count)
    for i in range(0, len(text) - k + 1):
        if count[i] == maxcount:
            frequentspatterns.append(text[i:i+k])
    frequentspatterns = list(set(frequentspatterns))
    return frequentspatterns


text = input()
k = int(input())

FrequentWords(text, k)
