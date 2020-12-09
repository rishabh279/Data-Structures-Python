def reverse_array(arr):
    """ Reverse given array"""
    n = len(arr)
    for i in range(int(n/2)):
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp
    return arr


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    arr = reverse_array(arr)
    print(arr)