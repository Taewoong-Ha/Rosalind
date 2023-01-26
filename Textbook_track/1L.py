'''
Implement PatternToNumber
Convert a DNA string to a number.
Given: A DNA string Pattern.
Return: PatternToNumber(Pattern).
Sample Dataset: AGT
Output: 11
'''


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

if __name__ == "__main__":
    with open('/Users/hataewoong/Downloads/rosalind_ba1l.txt', 'r') as f:
        lines = f.readlines()
        pattern = lines[0].strip()
        
    print(PatternToNum(pattern))
