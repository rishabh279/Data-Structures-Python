from trees.utils import Node


def convert_to_bt_dll_approach1(root):
    """ Convert the given binary tree into double linked list. """
    if root.left is not None:
        ltree = convert_to_bt_dll_approach1(root.left)
        while ltree.right:
            ltree = ltree.right
        ltree.right = root
        root.left = ltree

    if root.right is not None:
        rtree = convert_to_bt_dll_approach1(root.right)
        while rtree.left:
            rtree = rtree.left
        rtree.left = root
        root.right = rtree

    return root


def convert_to_bt_dll_approach2(root):
    pass


def convert_to_bt_dll_approach3(root):
    pass


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    convert_to_bt_dll_approach1(root)








