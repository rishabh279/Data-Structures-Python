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


def subarray_sum_second_approach(arr, sum):
    """
    Given an unsorted array, find a continuous subarray which adds to a given number
    """
    temp = {}
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        temp[current_sum] = i
        if type(temp.get(current_sum - sum)) == int:
            print(arr[temp[current_sum - sum]+1:i+1])
            break


def subarray_sum_third_approach(arr, val):
    """
    Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number
    """
    left = 0
    right = 0
    while left <= right:
        curr_sum = sum(arr[left:right + 1])
        if curr_sum > val:
            left += 1
        elif curr_sum < val:
            right += 1
        elif curr_sum == val:
            print(arr[left:right+1])
            break


if __name__ == '__main__':
    arr = [5, 4, 6, 7, 9, 8, 3, 1, 2]
    val = 21
    #arr = [8, 5, -2, 3, 4, -5, 7]
    #val = 10
    subarray_sum_third_approach(arr, val)
