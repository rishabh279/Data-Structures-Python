def get_equal_0_and_1(arr):
    """
    Find largest subarray with equal no of 0s and 1s
    """
    count = 0
    counts = {}
    max_length = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count += -1
        else:
            count += 1
        if count in counts:
            max_length = max(i-counts[count], max_length)
        else:
            counts[count] = i
    return max_length


if __name__ == '__main__':
    arr = [1, 0, 1, 1, 1, 0, 0]
    print(get_equal_0_and_1(arr))