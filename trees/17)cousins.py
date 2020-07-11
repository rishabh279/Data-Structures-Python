from trees.utils import Node


def is_cousin(node, a, b, level):
    """ Check given binary tree is counsin or not. """
    if get_level(node, a, level) == get_level(node, b, level) and not siblings(node, a, b):
        return 1
    else:
        return 0


def get_level(node, a, level):
    """ Get the level of given node in binary tree. """
    if node is None:
        return 0
    if node == a:
        return level
    left = get_level(node.left, a, level+1)
    if left != 0:
        return left

    return get_level(node.right, a, level+1)


def siblings(node, a, b):
    """ Check whehter two given nodes are binary tree or not. """
    if node is None:
        return None

    return (node.left == a and node.right == b) or (node.left == b and node.right == a) or siblings(node.left, a, b)\
           or siblings(node.right, a, b)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(15)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)

    node1 = root.left.right.right
    node2 = root.right.left.right

    print(is_cousin(root, node1, node2, 1))
