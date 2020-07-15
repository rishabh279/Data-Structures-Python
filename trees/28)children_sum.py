from trees.utils import Node, pre_order_traversal


def increment_child(node, diff):
    """ increment the children by diff """
    if node is None:
        return
    if node.left is not None:
        increment_child(node.left, diff)
        node.left.data = node.left.data + diff
    elif node.right is not None:
        increment_child(node.right, diff)
        node.right.data = node.right.data + diff

    return node


def children_sum(node):
    """ children sum property """
    if node.left is None and node.right is None:
        return
    else:
        children_sum(node.left)
        children_sum(node.right)
        if node.left is not None:
            left_data = node.left.data
        if node.right is not None:
            right_data = node.right.data
        diff = left_data + right_data - node.data
        if diff > 0:
            node.data = node.data + diff
        else:
            increment_child(node, -diff)

    return node


if __name__ == '__main__':
    root = Node(50)
    root.left = Node(7)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(30)
    node = children_sum(root)
    pre_order_traversal(node)