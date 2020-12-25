def zero_closest(arr):
    """
    Given_an_array_A__find_two_element_whose_sum_is_is_closest_to_zero
    """
    left = 0
    right = len(arr) - 1
    arr = sorted(arr)
    print(arr)
    closest_sum = 10000
    while left < right:
        curr_sum = arr[left] + arr[right]
        if abs(curr_sum) < abs(closest_sum):
            closest_sum = curr_sum
        if curr_sum < 0:
            left += 1
        else:
            right -= 1

    return closest_sum


if __name__ == '__main__':
    arr = [1, 60, -10, 70, -80, 85]
    print(zero_closest(arr))