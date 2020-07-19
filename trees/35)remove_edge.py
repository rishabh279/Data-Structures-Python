from trees.utils import Node


def count_no_of_nodes(node, size):
    """Checks removing an edge from binary tree can divide it into two halfs"""
    if node is None:
        return False
    count = count_no_of_nodes(node.left, size) + 1 + count_no_of_nodes(node.right, size)

    if count == size - count:
        print('1')

    return count


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(1)
    root.right = Node(6)
    root.left.left = Node(3)
    root.right.left = Node(7)
    root.right.right = Node(4)
    count_no_of_nodes(root, 6)