def mutable(string):
    """ Converts given string to list"""
    arr = []
    for i in string:
        arr.append(i)
    return arr


def check_string_rotation(string1, string2):
    """Checks two given strings are rotations of each other"""
    if len(string1) == len(string2):
        concat_string = string1 + string1
        if string2 in concat_string:
            print('True')
        else:
            print('False')


if __name__ == '__main__':
    check_string_rotation('abc', 'bca')