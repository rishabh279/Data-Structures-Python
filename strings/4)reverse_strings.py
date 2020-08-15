from strings.utils import string_to_list


def reverse_strings(string):
    """Reverse the given String"""
    arr = string_to_list(string)
    start = 0
    end = len(arr) - 1
    while start < end:
        temp = arr[start]
        arr[start] = arr[end-1]
        arr[end-1] = temp
    return arr


if __name__ == '__main__':
    reverse_strings()