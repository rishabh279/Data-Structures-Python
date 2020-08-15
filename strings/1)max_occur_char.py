def max_occur_char_approach_1(arr):
    """Find max occurred character using brute force"""
    max_count = 0
    max_char = ''
    for i in range(len(arr)):
        count = 1
        char = ''
        for j in range(i+ 1, len(arr)):
            if arr[i] == arr[j]:
                count += 1
                char = arr[i]
        if count > max_count:
            max_count = count
            max_char = char
    print(f'Most Frequent Character {max_char}')
    print(f'Count {max_count}')


def max_occur_char_approach_2(arr):
    """Find max occurred character using sorting"""
    arr.sort()
    max_count = 1
    count = 1
    max_char = ''
    print(arr)
    for i in range(len(arr)):
        if i < len(arr)-1:
            char = arr[i]
            if arr[i] == arr[i+1]:
                count = count + 1
            if count > max_count and char != arr[i+1]:
                max_count = count
                max_char = char
                count = 1
            elif char != arr[i+1]:
                count = 1
    print(f'Most Frequent Character {max_char}')
    print(f'Count {max_count}')


def max_occur_char_approach_3(arr):
    """Find max occurred character using BST"""
    pass


def max_occur_char_approach_4(arr):
    """Find max occurred character using HashTable"""
    hash = {}
    max_count = 0
    for i in arr:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1
    for key, value in hash.items():
        count = value
        if count > max_count:
            max_count = count
            max_char = key
    print(f'Most Frequent Character {max_char}')
    print(f'Count {max_count}')


if __name__ == '__main__':
    arr = ['R', 'I', 'S', 'H', 'A', 'B', 'H', 'R', 'R', 'A', 'A', 'A', 'R', 'R', 'R']
    max_occur_char_approach_4(arr)
