def search_in_sorted_rotated_array(arr, num):
    """Rotate a matrix by 90 degree in clockwise direction without using any extra space"""
    if len(arr) < 0:
        return 0

    left = 0
    right = len(arr) - 1

    for i in range(left, right):
        if left < right:
            mid = left + int((right - left) / 2)
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid

    start = left
    left = 0
    right = len(arr) - 1

    if num >= arr[start] and num <= arr[right]:
        left = start
    else:
        right = start - 1

    for i in range(left, right):
        mid = left + int((right - left) / 2)
        if num > arr[mid]:
            left = mid + 1
        elif num < arr[mid]:
            right = mid - 1
        elif num == arr[mid]:
            return mid


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    print(search_in_sorted_rotated_array(arr, 3))