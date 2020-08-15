def concat_zigzag(string, n):
    """Print concatenation of zigzag string in n rows. """
    row = 0
    arr = ["" for _ in range(n)]

    for i in range(len(string)):

        arr[row] += string[i]

        if row == n-1:
            down = False
        elif row == 0:
            down = True

        if down:
            row += 1
        else:
            row -= 1
    s = ''
    for j in range(n):
        s += arr[j]
    print(s)


if __name__ == '__main__':
    concat_zigzag('GEEKSFORGEEKS', 3)
