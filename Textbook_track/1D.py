# Find All Occurrences of a Pattern in a String

def PatternInString(string, pattern):
    count = ""
    for i in range(0, len(string) - len(pattern)):
        sub = string[i:i+len(pattern)]
        if sub == pattern:
            count = count + str(i) + " "
        else:
            pass
    return print(count)

string = input()
pattern = input()

PatternInString(string, pattern)
