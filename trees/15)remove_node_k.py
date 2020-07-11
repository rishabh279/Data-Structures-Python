from trees.utils import Node, pre_order_traversal


def remove_nodes(node, k):
    """ Remove nodes on root to leaf paths of length < K """
    if node is None:
        return None
    if k == 0:
        return node

    node.left = remove_nodes(node.left, k-1)
    node.right = remove_nodes(node.right, k-1)

    if node.left == None and node.right == None:
        return None
    return node


if __name__ == '__main__':
    k = 4
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)
    root.right.right = Node(6)
    root.right.right.left = Node(8)
    pre_order_traversal(root)
    remove_nodes(root, k)
    print('After Removal')
    pre_order_traversal(root)



