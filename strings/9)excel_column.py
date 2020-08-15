def excel_column_name(n):
    """Prints the excel column name from given column number"""
    string = ''
    i = 0
    while n > 0:
        rem = n % 26
        if rem == 0:
            string += 'Z'
            n = int(n / 26) - 1
            i += 1
        else:
            string += chr((rem-1) + ord('A'))
            n = int(n / 26)
            i += 1
    return string[::-1]


if __name__ == '__main__':
    print(excel_column_name(52))