def get_equilibrium_index(arr):
    """Find_the_equilibrium_index_in_an_array_apprach-1"""
    sum = 0
    n = len(arr)
    left_sum = [0] * n
    right_sum = [0] * n
    for i in range(n):
        sum += arr[i]
        left_sum[i] = sum

    sum = 0
    j = n - 1
    while j >= 0:
        sum += arr[j]
        right_sum[j] = sum
        j -= 1

    for i in range(n):
        if left_sum[i] == right_sum[i+1] and i < n-1:
            return i


if __name__ == '__main__':
    arr = [10, 5, 15, 3, 4, 21, 2]
    print(get_equilibrium_index(arr))


