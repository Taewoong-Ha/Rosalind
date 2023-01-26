def SymbolToNum(symbol):
    if symbol == "":
        raise ValueError("No symbol. enter the symbol was passed.")
    if symbol == "A":
        num = 0
    elif symbol == "C":
        num = 1
    elif symbol == "G":
        num = 2
    elif symbol == "T":
        num = 3
    return num

def PreFix(pattern):
    return pattern[:-1]

def LastSymbol(pattern):
    return pattern[-1]

def FindOtherSymbol(pattern):
    pattern = pattern.replace('A','')
    pattern = pattern.replace('G','')
    pattern = pattern.replace('C','')
    pattern = pattern.replace('T','')
    return pattern


def PatternToNum(pattern):
    pattern = pattern.upper()
    
    if len(FindOtherSymbol(pattern)) > 0:
        raise ValueError("Confirm the DNA Seq. Find {0}".format(FindOtherSymbol(pattern)))
    
    if pattern == "":
        return 0
    
    symbol = LastSymbol(pattern)
    prefix = PreFix(pattern)
    return 4 * PatternToNum(prefix) + SymbolToNum(symbol)

def ComputingFrequencies(text, k):
    frequency_array = [0 for i in range(4**k)]
    
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k ]
        j = PatternToNum(pattern)
        frequency_array[j] = frequency_array[j] + 1
    return frequency_array
  
  
 ############### Fasterfrequentwords(text,k)
def FasterFrequentWords(text, k):
    frequent_patterns = set()
    frequency_array = ComputingFrequencies(text, l)
    max_count = max(frequency_array)
    for i in range(4**k):
        if frequency_array[i] == max_count:
            pattern = NumToPattern(i, k)
            
    
def NumToSymbol(num):
    if num > 4:
        raise ValueError("No symbol. confrim {0}".format(i))
    if num == 0:
        symbol = "A"
    elif num == 1:
        symbol = "C"
    elif num == 2:
        symbol = "G"
    elif num == 3:
        symbol = "T"
    return symbol
  

def NumToPattern(index, k):
    if k == 1:
        return NumToSymbol(index)
  
  

if __name__ == "__main__":
#     text  = "AAA"
#     k = 2
#     print(" ".join(map(str,ComputingFrequencies(text, k))))
    with open('/Users/hataewoong/Downloads/rosalind_ba1k-3.txt', 'r') as f:
        lines = f.readlines()
        text = lines[0].strip()
        k = int(lines[1].strip())
         

    with open('/Users/hataewoong/Downloads/ba1k_result.txt', 'w') as f:
        f.write(" ".join(map(str,ComputingFrequencies(text, k))))
        f.close()

        
        
