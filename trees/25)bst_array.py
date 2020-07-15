from trees.utils import Node


def bst(start, end, arr):
    """ Convert given sorted array to balanced BST"""

    if end < start:
        return

    mid = (start + end) / 2
    mid = int(mid)

    newnode = Node(arr[mid])
    newnode.left = bst(start, mid-1, arr)
    newnode.right = bst(mid+1, end, arr)

    return newnode


if __name__ == '__main__':
    arr = [5, 10, 20, 30, 40, 50, 55]
    bst(0, len(arr)-1, arr)
