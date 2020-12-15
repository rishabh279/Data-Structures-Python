def trapping_rainwater(arr):
    """ Trapping Rainwater Problem """
    n = len(arr)
    left = [0] * n
    right = [0] * n
    max_elem = -1
    total_water = 0
    for i in range(n):
        max_elem = max(arr[i], max_elem)
        left[i] = max_elem

    max_elem = -1
    for i in range(n-1, -1, -1):
        max_elem = max(max_elem, arr[i])
        right[i] = max_elem

    for i in range(n):
        min_elem = min(left[i], right[i])
        total_water += abs(arr[i]-min_elem)

    return total_water


if  __name__ == '__main__':
    arr = [1, 0, 2, 0, 1, 0, 3, 1, 0, 2]
    print(trapping_rainwater(arr))