
def mutable(str):
    """Convert string to list"""
    arr = []
    for i in str:
        arr.append(i)
    return arr


def remove_duplciates_1(string):
    """Remove duplicates from given string"""
    arr = []
    for i in range(len(string)):
        if string[i] not in arr:
            arr.append(string[i])
    return ''.join(arr)


def remove_duplciates_2(string):
    """Remove duplicates from given string"""
    hash = [0] * 256
    arr = mutable(string)
    i = 0
    for j in range(len(arr)):
        if hash[ord(arr[j])] == 0:
            hash[ord(arr[j])] = 1
            arr[i] = arr[j]
            i = i + 1
    return ''.join(arr[0:i])


if __name__ == '__main__':
    print(remove_duplciates_1('xgboost'))
