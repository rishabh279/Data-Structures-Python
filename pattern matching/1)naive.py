
def pattern_match(str1, str2):
    """ Returns the indexes of all occurrences of pattern str2 found in the string str1"""
    for i in range(len(str1)-len(str2)):
        for j in range(len(str2)):
            if str2[j] != str1[i+j]:
                break
        if j == len(str2)-1:
            print(f"Pattern found at index {i} ")


if __name__ == '__main__':
    pattern_match("AABAACAADAABAAABAA", "AABA")