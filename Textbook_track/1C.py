# Find the Reverse Complement of a String

def ReverseComplement(pattern):
    reverse_pattern = pattern[::-1]
    reverse_complement = ""
    for i in range(0, len(reverse_pattern)):
        if reverse_pattern[i] == "A":
            reverse_complement += "T"
        elif reverse_pattern[i] == "C":
            reverse_complement += "G"
        elif reverse_pattern[i] == "G":
            reverse_complement += "C"
        else:
            reverse_complement += "A"
    return reverse_complement

pattern = input()

ReverseComplement(pattern)
