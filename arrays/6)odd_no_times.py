def count_odd_no(arr):
    """Find the number occurring odd number of times in given array given that there is only one number which
    occurs odd no. of times"""
    temp = 0
    for i in arr:
        temp = temp ^ arr[i]
    print(temp)


if __name__ == '__main__':
    arr = [1, 2, 1, 3, 1, 4]
    count_odd_no(arr)