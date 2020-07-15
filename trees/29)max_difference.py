from trees.utils import Node


def max_diff(node, res):
    """ Calculate max of all differences between node and its ancestor """
    if node is None:
        return 99999, res

    if node.left is None and node.right is None:
        return node.data, res

    left_data, res = max_diff(node.left, res)
    right_data, res = max_diff(node.right, res)
    minimum = min(left_data, right_data)
    res = max(res, node.data-minimum)

    return min(minimum, node.data), res


if __name__ == '__main__':
    root = Node(8)
    root.left = Node(3)

    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)

    root.right = Node(10)
    root.right.right = Node(14)
    root.right.right.left = Node(13)

    min_elem, diff = max_diff(root, -9999)
    print(diff)