from trees.utils import create_static_tree, pre_order_traversal


def reverse_alternate(node1, node2, level):
    """Reverse alternate levels of perfect binary tree"""
    if node1 is None or node2 is None:
        return
    if level % 2 == 0:
        temp = node1.data
        node1.data = node2.data
        node2.data = temp

    reverse_alternate(node1.left, node2.right, level+1)
    reverse_alternate(node1.right, node2.left, level+1)


if __name__ == '__main__':
    root = create_static_tree()
    pre_order_traversal(root)
    reverse_alternate(root.left, root.right, 1)
    print('After Reversing')
    pre_order_traversal(root)