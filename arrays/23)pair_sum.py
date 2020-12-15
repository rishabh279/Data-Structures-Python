def get_pair_sum(arr, elem):
    """Find_a_pair_an_array_whose_sum_equal_to_given_no"""
    n = len(arr)
    map = [0] * 1000
    count = 0
    for i in range(n):
        map[arr[i]] += 1

    for i in range(n):
        index = elem - arr[i]

        count += map[index]

        if index == arr[i]:
            count -= 1

    return int(count/2)


if __name__ == '__main__':
    arr = [1, 1, 1, 1]
    print(get_pair_sum(arr, 2))