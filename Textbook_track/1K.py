'''
Given an integer k, we define the frequency array of a string Text as an array of length 4k, 
where the i-th element of the array holds the number of times that the i-th k-mer 
(in the lexicographic order) appears in Text (see Figure 1.

Computing a Frequency Array
Generate the frequency array of a DNA string.

Given: A DNA string Text and an integer k.
Return: The frequency array of k-mers in Text.

Sample Dataset: ACGCGGCTCTGAAA 2
Sample Output: 2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0
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

def ComputingFrequencies(text, k):
    frequency_array = [0 for i in range(4**k)]
    
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k ]
        j = PatternToNum(pattern)
        frequency_array[j] = frequency_array[j] + 1
    return frequency_array

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
