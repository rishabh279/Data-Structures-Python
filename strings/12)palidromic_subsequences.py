
def check_palidrome(string):
    """ Check given string is palidrome or not. """
    start = 0
    end = len(string) -1
    while start<end:
        if string[start] != string[end]:
            return 0
        start += 1
        end -= 1
    return 1


def palidromic_subsequences(string):
    """ Minimum number of palindromic subsequences to be removed to empty a balanced tree """
    if check_palidrome(string):
        print('1')
    else:
        print('2')

if __name__ == '__main__':
    palidromic_subsequences('11101')