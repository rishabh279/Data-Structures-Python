def same_set_of_digits(arr):
    """
    Next_greater_number_with_same_set_of_digits.
    """
    n = len(arr)
    j = 0
    replace_index = -1
    least_greater_elem = 1000000000
    least_greater_elem_index = -1
    for i in range(n-1, -1, -1):
        if arr[i-1] < arr[i]:
            replace_index = i-1
            break

    if i == 0 and arr[i+1] < arr[i]:
        print("Not possible")
        return

    for i in range(n - 1, replace_index, -1):
        if arr[i] < least_greater_elem:
            least_greater_elem = arr[i]
            least_greater_elem_index = i

    temp = arr[least_greater_elem_index]
    arr[least_greater_elem_index] = arr[replace_index]
    arr[replace_index] = temp

    sorted_number = sorted(arr[replace_index+1:])

    for i in range(replace_index+1, n):
        arr[i] = sorted_number[j]
        j+=1

    print(arr)


if __name__ == '__main__':
    arr = [2, 1, 8, 7, 6, 5]
    same_set_of_digits(arr)