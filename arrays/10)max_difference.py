def max_difference(arr):
    """Find the maximum difference between two elements such that larger element appears after the smaller element."""
    diff_arr = []
    n = len(arr)
    for i in range(n):
        if i < n-1:
            diff_arr.append(arr[i+1] - arr[i])

    max = diff_arr[0]
    for i in range(1, len(diff_arr)):
        if diff_arr[i-1] > 0:
            diff_arr[i] += diff_arr[i-1]

        if diff_arr[i] > max:
            max = diff_arr[i]
    print(f"Diff arr is {diff_arr}")
    print(f"Maximum Diff is {max}")


if __name__ == '__main__':
    arr = [3, 1, 4, 7, 5, 100, 10]
    max_difference(arr)