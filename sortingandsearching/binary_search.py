def binary_search(arr, elem):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + int((right - left) / 2)
        if arr[mid] > elem:
            right = mid - 1
        elif arr[mid] < elem:
            left = mid + 1
        elif arr[mid] == elem:
            print('Element found at', mid)
            return
    print('Element not present in array.')


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    elem = 2
    binary_search(arr, elem)