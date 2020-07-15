from trees.utils import create_static_tree
from collections import OrderedDict


def left_view(node, level, max):
    """Print the left view of Binary Tree"""
    if node is None:
        return None

    if level > max[0]:
        print(node.data)
        max[0] = level
    left_view(node.left, level+1, max)
    left_view(node.right, level+1, max)


def top_view(node, height, hd, m):
    """ Finds the top view of Binary Tree """
    if node == None:
        return

    if hd not in m:
        m[hd] = [node.data, height]
    else:
        p = m[hd]
        if p[1] > height:
            m[hd] = [node.data, height]

    top_view(node.left, height + 1, hd - 1, m)
    top_view(node.right, height + 1, hd + 1, m)


def bottom_view(node, height, hd, m):
    """ Finds the bottom view of Binary Tree """
    if node == None:
        return

    if hd not in m:
        m[hd] = [node.data, height]
    else:
        p = m[hd]
        if p[1] <= height:
            m[hd] = [node.data, height]

    bottom_view(node.left, height + 1, hd - 1, m)
    bottom_view(node.right, height + 1, hd + 1, m)


def print_view(root, bottom=False):
    """ Prints the top view of Binary Tree"""
    m = OrderedDict()
    if not bottom:
        top_view(root, 0, 0, m)
    else:
        bottom_view(root, 0, 0, m)

    for i in sorted(list(m)):
        p = m[i]
        print(p[0], end=" ")


if __name__ == '__main__':
    # Left View
    # root = Node(12)
    # root.left = Node(10)
    # root.right = Node(20)
    # root.right.left = Node(25)
    # root.right.right = Node(40)
    # left_view(root, 1, [0])

    #Top View & Bottom View
    print_view(create_static_tree(), True)
