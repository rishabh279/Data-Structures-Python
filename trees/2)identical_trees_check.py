from trees.utils import create_static_tree


def check_identical(node1, node2):
    """ Check if two trees are identical or not"""
    if node1 is None and node2 is None:
        return 1
    if node1 is not None and node2 is not None:
        return node1.data == node2.data and check_identical(node1.left, node2.left) and \
               check_identical(node1.right, node2.right)
    return 0


if __name__ == '__main__':
    tree1 = create_static_tree()
    tree2 = create_static_tree()
    if check_identical(tree1, tree2) == 1:
        print("Identical")
    else:
        print("Not Identical")