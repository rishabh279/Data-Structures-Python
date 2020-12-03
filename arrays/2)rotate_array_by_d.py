
def reverse_array(arr, start, end):
    """ Reverse array """
    for i in range(start, end):
        if i < end:
            temp = arr[i]
            arr[i] = arr[end - 1]
            arr[end - 1] = temp
            end = end - 1
    return arr


def rotate_array(arr, n, d):
    """ Rotate the given array of size n by d elements. """
    arr = reverse_array(arr, 0, d)
    arr = reverse_array(arr, d, n)
    arr = reverse_array(arr, 0, n)

    return arr


if __name__ == '__main__':
    arr = [5, 6, 4, 3, 2, 0]
    print(rotate_array(arr, 6, 2))