from trees.utils import create_static_bst


def lca(node, a, b):
    """ Return the least common ancestor of given inputs in binary search tree. """
    if node is None:
        return 0
    elif a < node.data and b < node.data:
        return lca(node.left, a, b)
    elif a > node.data and b > node.data:
        return lca(node.right, a, b)
    return node


def lca_iterative(node, a, b):
    """ Return the least common ancestor of given inputs in binary search tree in an iterative manner"""
    while(node):
        if node is None:
            return 0
        elif a < node.data and b < node.data:
            node = node.left
        elif a > node.data and b > node.data:
            node = node.right
        else:
            break
    return node


if __name__ == '__main__':
    root = create_static_bst()
    print(lca(root, 16, 40).data)
    print(lca_iterative(root, 16, 40).data)