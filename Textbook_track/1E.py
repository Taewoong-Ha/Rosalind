import re

def PatternCount(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern) +1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count


  
def FrequentWords(text, k, t):
    frequentspatterns = []
    count = []
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]
        count.append(PatternCount(text, pattern))
    maxcount = t
    for i in range(0, len(text) - k + 1):
        if count[i] == maxcount:
            frequentspatterns.append(text[i:i+k])
    frequentspatterns = list(set(frequentspatterns))
    return frequentspatterns
  
  def FindClump(genome, k, L):
    clump = []
    for i in range(0, len(genome) - L + 1):
        sub = genome[i:i+L]
        clump.append(FrequentWords(sub, k, t))
    tuple_clump = [tuple(l) for l in clump]
    clump = list(set(tuple_clump))
    
    unique = ""
    for i in range(0, len(clump)):
        aa = ""
        aa = str(clump[i])
        aa = re.sub(r"[^a-zA-Z]", "", aa) 
        if aa == "":
            pass
        else:
            unique = unique + aa + " "
    return print(unique)



genome = input()
k = int(input())
L = int(input())
t = int(input())

FindClump(genome, k, L)
