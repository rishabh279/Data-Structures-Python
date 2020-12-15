def subarray_sum_first_approach(arr, sum):
    """
    Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number
    """
    for i in range(len(arr)):
        temp_arr = []
        curr_sum = arr[i]
        temp_arr.append(arr[i])
        for j in range(i+1, len(arr)):
            curr_sum += arr[j]
            temp_arr.append(arr[j])
            if curr_sum == sum:
                print(temp_arr)
                return


if __name__ == '__main__':
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    sum = 23
    subarray_sum_first_approach(arr, sum)