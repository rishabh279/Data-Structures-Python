from trees.utils import Node, pre_order_traversal


def sum_tree(node):
    """ Convert the given binary tree into sum tree"""
    if node is None:
        return 0

    left_sum = sum_tree(node.left)
    right_sum = sum_tree(node.right)
    previous = node.data
    node.data = left_sum + right_sum

    return node.data + previous


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(6)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    root.right.left = Node(7)
    root.right.right = Node(5)
    sum_tree(root)
    pre_order_traversal(root)
