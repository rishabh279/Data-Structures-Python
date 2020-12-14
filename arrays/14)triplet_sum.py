def triplet_sum(arr, num):
    """Find_a_triplet_in_given_array_that_sum_to_given_value x"""
    n = len(arr)
    for i in range(n):
        fixed = arr[i]
        j = i + 1
        while j < n-1:
            current = fixed + arr[j] + arr[n-1]
            if current < num:
                j += 1
            elif current > num:
                n -= 1
            else:
                print((fixed, arr[j], arr[n-1]))
                return 0


if __name__ == '__main__':
    arr = [1, 2, 5, 6, 9, 10]
    triplet_sum(arr, 15)



