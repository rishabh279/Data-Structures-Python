def wave_form_approach1(arr):
    """
    Given an array of integers, sort the array into a wave like array and return it.
    (arrange the element into a sequence such that a1>=a2<=a3>=a4<=a5)
    T.C-O(nlog(n))
    """
    arr.sort()
    for i in range(0, len(arr)-1, 2):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp

    print(arr)


def wave_form_approach2(arr):
    """
    Given an array of integers, sort the array into a wave like array and return it.
    (arrange the element into a sequence such that a1>=a2<=a3>=a4<=a5)
    T.C-O(n)
    """
    for i in range(0, len(arr), 2):
        if i-1 > 0 and arr[i] < arr[i-1]:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp

        if i < len(arr)-1 and arr[i] < arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    print(arr)


if __name__ == '__main__':
    #arr = [1, 2, 3, 4, 5, 6, 7, 8]
    arr = [20, 8, 10, 6, 4, 2]
    #wave_form_approach1(arr)
    wave_form_approach2(arr)