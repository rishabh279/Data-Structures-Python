def length_encoding(string):
    """Returns the run length encoded string of given input string"""
    encoded_string = ''
    i = 0
    while i < len(string)-1:
        count = 1
        encoded_string += string[i]
        for j in range(i, len(string)-1):
            if string[j] == string[j+1]:
                count += 1
            else:
                break
        encoded_string += str(count)
        i = j + 1
    return encoded_string


if __name__ == '__main__':
    print(length_encoding('aaabbbbddeee'))