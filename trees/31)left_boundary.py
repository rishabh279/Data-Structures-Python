from trees.utils import Node


def print_left_boundary(node):
    """ Print left boundary of binary tree """
    if node is None:
        return None
    if node.left is not None:
        print(node.data)
        print_left_boundary(node.left)
    elif node.right is not None:
        print(node.data)
        print_left_boundary(node.right)


def print_right_boundary(node):
    """ Print right boundary of binary tree """
    if node is None:
        return None
    if node.right is not None:
        print(node.data)
        print_left_boundary(node.right)
    elif node.left is not None:
        print(node.data)
        print_left_boundary(node.left)


def print_leaves(node):
    """ Print leaves of binary tree """
    if node is None:
        return None
    print_leaves(node.left)
    if node.left is None and node.right is None:
        print(node.data)
    print_leaves(node.right)


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    print_left_boundary(root)
    print_leaves(root)
    print_right_boundary(root)