def get_triangles(arr):
    """
    Algorithm_for_number_of_possible_triangles.
    """
    arr = sorted(arr)
    n = len(arr)
    total_triangles = 0
    for i in range(n-2):
        k = i + 2
        for j in range(i+1, n-1):
            while k < n and (arr[i] + arr[j] > arr[k]):
                k += 1
            if k > j:
                total_triangles += k - j - 1
    return total_triangles


if __name__ == '__main__':
    arr = [6, 7, 8, 10, 12, 14, 50]
    print(get_triangles(arr))