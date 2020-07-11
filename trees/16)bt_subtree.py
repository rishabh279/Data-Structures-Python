from trees.utils import Node


def identical_tree(tree1, tree2):
    """ Check whether two given trees are identical or not """
    if tree1 is None and tree2 is None:
        return 1
    if tree1 is not None and tree2 is not None:
        return tree1.data == tree2.data and identical_tree(tree1.left, tree2.left) and \
               identical_tree(tree1.right, tree2.right)

    return 0


def bt_subtree_approach1(tree, subtree):
    """ Check whether tree is a sub-tree of given binary subtree """
    if tree is None:
        return 0
    if tree.data == subtree.data:
        if identical_tree(tree, subtree) == 1:
            print('subtree is present in given binary tree')
            return 1
    return bt_subtree_approach1(tree.left, subtree) or bt_subtree_approach1(tree.right, subtree)


def bt_subtree_approach(tree, subtree):
    pass


if __name__ == '__main__':
    T = Node(26)
    T.right = Node(3)
    T.right.right = Node(3)
    T.left = Node(10)
    T.left.left = Node(4)
    T.left.left.right = Node(30)
    T.left.right = Node(6)

    S = Node(10)
    S.right = Node(6)
    S.left = Node(4)
    S.left.right = Node(30)

    bt_subtree_approach1(T, S)

