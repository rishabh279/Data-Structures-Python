def remove_adjacent_duplicates(string):
    """Remove all adjacent duplicates in string"""
    stack = []

    for j in range(len(string)):
        print(j)
        if j == 0:
            stack.append(string[j])
        elif stack and stack[-1] == string[j]:
            stack.pop()
        else:
            stack.append(string[j])


if __name__ == '__main__':
    remove_adjacent_duplicates('abbaca')
    #print([1, 2].pop())