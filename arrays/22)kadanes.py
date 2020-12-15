def get_max_sum_subarray(arr):
    """
    Algorithm to find the contiguous sub-array with maximum sum, for a given array of postive and negative numbers.
    """
    n = len(arr)
    max_sum = arr[0]
    current_max = arr[0]
    for i in range(1, n):
        current_max = max(arr[i], current_max + arr[i])
        max_sum = max(current_max, max_sum)
    return max_sum


if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(get_max_sum_subarray(arr))