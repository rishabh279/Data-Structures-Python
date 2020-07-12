from trees.utils import Node
from collections import defaultdict


def diagonal_traversal(node, level, diagonal):
    """ Diagonal traversal of binary tree """
    if node is None:
        return None
    diagonal[level].append(node.data)

    diagonal_traversal(node.left, level+1, diagonal)
    diagonal_traversal(node.right, level, diagonal)

    return diagonal


if __name__ == '__main__':
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    diagonal = defaultdict(list)
    diagonal_traversal(root, 0, diagonal)
    print(diagonal)
