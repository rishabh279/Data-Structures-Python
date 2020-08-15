def check_anagram(str1, str2):
    """Check given strings are anagram or not"""
    count = [0] * 256

    if len(str1) == len(str2):
        for i in str1:
            count[ord(i)] += 1

        for i in str2:
            count[ord(i)] -= 1

        for i in range(256):
            if count[i] != 0:
                print('Not Anagram')
                return
        print('Anagram')
    else:
        print('Not Anagram')


if __name__ == '__main__':
    check_anagram('heater', 'reheat')