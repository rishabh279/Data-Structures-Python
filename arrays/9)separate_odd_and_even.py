def separate_odd_and_even(arr):
    """ Segregate odd and even no                                                                                   s in an array. """
    n = len(arr)
    left = 0
    right = n-1
    for i in range(n):
        if left < right:
            if arr[left]%2 == 0:
                left += 1
            if arr[right]%2 == 1:
                right -= 1
            if arr[left]%2 == 1 and arr[right]%2 == 0:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                left += 1
                right -= 1
    return arr


if __name__ == '__main__':
    arr = [2, 3, 4, 7, 6, 8, 11, 13, 17, 10]
    arr = separate_odd_and_even(arr)
    print(arr)
    [1, 1, 3, ]