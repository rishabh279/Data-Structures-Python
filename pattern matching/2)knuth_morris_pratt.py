
def kmp(text, patt, lps):
    """Find the occurrences of pattern in string using Knuth Morris Pratt Algorithm"""
    j = 0
    for i in range(len(text)):
        if text[i] == patt[j]:
            i += 1
            j += 1

        if j == len(patt):
            print(f'Pattern found at {i-j}')
            j = lps[j-1]
        elif i < len(text) and text[i] != patt[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


