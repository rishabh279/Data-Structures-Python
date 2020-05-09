from trees.utils import create_static_tree


def binary_tree_size(node):
    """ Finds size of binary tree. """
    if node is None:
        return 0
    return 1 + binary_tree_size(node.left) + binary_tree_size(node.right)


print(binary_tree_size(create_static_tree()))
