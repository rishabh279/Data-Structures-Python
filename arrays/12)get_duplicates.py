def get_duplicates(arr):
    """Algorithm to find duplicate elements in O(n) time and O(1) extra space, for a given array of size 'n'"""

    for i in range(len(arr)):
        if arr[abs(arr[i])] > 0:
            arr[abs(arr[i])] = arr[abs(arr[i])] * -1
        else:
            print(abs(arr[i]))


if __name__ == '__main__':
    arr = [4, 3, 1, 1, 2, 2, 3]
    get_duplicates(arr)