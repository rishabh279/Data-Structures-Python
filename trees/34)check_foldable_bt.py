from trees.utils import Node


def check_foldable_binary_tree(node1, node2):
    """Check whether binary tree is foldable or not"""
    if node1 is None and node2 is None:
        return True

    if node1 is None or node2 is None:
        return False

    return check_foldable_binary_tree(node1.left, node2.right) \
           and check_foldable_binary_tree(node1.right, node2.left)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    print(check_foldable_binary_tree(root.left, root.right))