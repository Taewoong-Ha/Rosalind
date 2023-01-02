
def patterncount(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern) +1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
  
  
  def count:
    pass
  
  def frequentwords(text, k):
    frequentpatterns = []
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]
        count[i] = patterncount(text, pattern)
    maxcount = max(count)
    for i in range(0, len(text) - k + 1):
        if count[i] == maxcount:
            frequentpatterns.append(text[i:i+k])
    list(set(frequentpatterns))
    return frequentpatterns

text = input()
k = int(input())

frequentwords(text, k)
