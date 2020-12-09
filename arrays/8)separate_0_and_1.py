def separate_0_and_1(arr):
    """ Segregate 0s and 1s in an array. """
    n = len(arr)
    left = 0
    right = n-1
    for i in range(n):
        if left < right:
            if arr[left] == 0:
                left += 1
            if arr[right] == 1:
                right -= 1
            if arr[right] != arr[left]:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                left += 1
                right -= 1
    return arr


if __name__ == '__main__':
    arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    arr = separate_0_and_1(arr)
    print(arr)