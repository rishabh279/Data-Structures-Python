def two_repeating_elements(arr):
    """ Algorithm to find two repeating numbers in a given array. """
    for i in range(len(arr)):
        if arr[abs(arr[i])] < 0:
            print(abs(arr[i]))
        elif arr[abs(arr[i])] > 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 1, 3]
    two_repeating_elements(arr)
