def first_non_repeating_character_1(string):
    """Returns the first non-repeating character in string"""
    for i in range(len(string)):
        if string[i] not in string[i+1:len(string)]:
            print(string[i])
            return


def first_non_repeating_character_2(string):
    """Returns the first non-repeating character in string"""
    hash = [0] * 256
    for i in string:
        if hash[ord(i)] == 0:
            hash[ord(i)] = 1
        else:
            hash[ord(i)] += 1

    for i in string:
        if hash[ord(i)] == 1:
            print(i)
            break


if __name__ == '__main__':
    first_non_repeating_character_2('RISRI')