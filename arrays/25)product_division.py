def get_product_division(arr):
    """
      Product_of_array_without_using_division_operator
    """
    n = len(arr)
    left = [0] * n
    right = [0] * n
    prod = 1
    for i in range(n):
        prod *= arr[i]
        left[i] = prod

    prod = 1
    for i in range(n-1, -1, -1):
        prod *= arr[i]
        right[i] = prod

    for i in range(n):
        if i == 0:
            arr[i] = right[i+1]
        elif i == n-1:
            arr[i] = left[i-1]
        else:
            arr[i] = left[i-1] * right[i+1]

    return arr


if __name__ == '__main__':
    arr = [10, 20, 30, 40]
    print(get_product_division(arr))