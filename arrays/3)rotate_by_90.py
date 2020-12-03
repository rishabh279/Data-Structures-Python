def rotate_by_90(arr):
    """ Rotate Image by 90. """
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            if i != j:
                temp = arr[i][j]
                arr[i][j] = arr[j][i]
                arr[j][i] = temp
    
    for i in range(n):
        for j in range(int(n/2)):
            temp = arr[i][j]
            arr[i][j] = arr[i][n-j-1]
            arr[i][n-j-1] = temp
    return arr


if __name__ == '__main__':
    arr = [[1, 2, 3],
           [6, 7, 8],
           [11, 12, 14]]
    print(rotate_by_90(arr))
