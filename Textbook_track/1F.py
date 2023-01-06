# Find a Position in a Genome Minimizing the Skew

# string = CATGGGCATCGGCCATACGCC
# G = +1, C = -1
# 0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

def Skew(genome):
    skew = [0]
    for i in range(len(genome)):
        if genome[i] == "G":
            skew.append(skew[-1] + 1)
        elif genome[i] == "C":
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])
    min_skew = min(skew)

    for i in range(len(skew)):
        if skew[i] == min_skew:
            print(i, end = " ")
    return 

if __name__ == "__main__":
    '''
    Given: A DNA string Genome.
    Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).
    Sample Dataset: "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"
    Sample Output: 53 97
    input1: 11 24 | input2: 3 | input3: 4 | input4: 2 | input5: 2 6 | input6: 89969 89970 89971 90345 90346
    '''
    with open("C:/Users/user/Downloads/rosalind_ba1f.txt", "r") as f:
        genome = f.readline().strip()
        
    Skew(genome)

    
