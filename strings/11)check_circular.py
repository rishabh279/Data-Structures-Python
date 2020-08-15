def check_circular(path):
    """Check whether given path is circular or Not"""
    N, E, S, W = 0, 1, 2, 3
    x, y, dir = 0, 0, N

    for i in range(len(path)):
        if path[i] == 'R':
            dir = (1 + dir) % 4
        elif path[i] == 'L':
            dir = (4 + dir -1) % 4
        elif path[i] == 'G':
            if dir == N:
                y += 1
            elif dir == S:
                y -= 1
            elif dir == E:
                x += 1
            elif dir == W:
                x -= 1

    return x == 0 and y == 0


if __name__ == '__main__':
    print(check_circular('GLGLGLG'))
