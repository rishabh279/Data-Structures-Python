def get_smallest_number(arr):
    """
    Smallest integer value that can't be represented as sum of any subset of a given array.
    """
    smallest_sum = -1
    arr = sorted(arr)
    for i in range(len(arr)):
        if i == 0:
            smallest_sum = arr[i] + 1
        elif arr[i] <= smallest_sum:
            smallest_sum += arr[i]
    return smallest_sum


if __name__ == '__main__':
    arr = [1, 2, 5, 10, 20, 40]
    print(get_smallest_number(arr))