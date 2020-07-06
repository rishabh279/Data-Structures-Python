from trees.utils import create_static_tree


def print_nodes(node, d, l):
    """ Print nodes after d-distance """
    if node is None:
        return -1
    if d == l:
        print(node.data)
        return
    print_nodes(node.left, d, l+1)
    print_nodes(node.right, d, l+1)


if __name__ == '__main__':
    print_nodes(create_static_tree(), 3, 0)
