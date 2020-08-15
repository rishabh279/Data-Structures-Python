def check_palindrome(string):
    """Checks given string is palindrome or not"""
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            print('Not Palindrome')
            return
        start += 1
        end -= 1
    print('Palindrome')


if __name__ == '__main__':
    string = 'MADAM'
    check_palindrome(string)