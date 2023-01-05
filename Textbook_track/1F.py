# Find a Position in a Genome Minimizing the Skew

# string = CATGGGCATCGGCCATACGCC
# G = +1, C = -1
# 0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

import numpy as np

        
        
def Skew(genome):
    count_str = [0]
    count = 0 
    for i in range(len(genome)):
        if genome[i] == "G":
            count += 1
            count_str.append(count)
        elif genome[i] == "C":
            count -= 1
            count_str.append(count)
        else:
            count_str.append(count_str[i-1])
    pos = np.where(np.array(count_str) == min(count_str))[0]
    return  pos

def print_Skew(genome):
    aa = Skew(genome)
    a = ""
    for i in aa:
        a = a + str(i) + " "
    print(a)

genome = input()

print_Skew(genome)


    
