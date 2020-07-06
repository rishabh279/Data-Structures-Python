from trees.utils import create_static_tree


def find_lca(node, a, b):
    """ Find least common ancestor of binary tree """
    if node is None:
        return node
    elif node.data == a or node.data == b:
        return node

    left = find_lca(node.left, a, b)
    right = find_lca(node.right, a, b)

    if left and right:
        return node

    return left if left is not None else right


if __name__ == '__main__':
    print(find_lca(create_static_tree(), 8, 11).data)