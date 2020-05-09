from trees.utils import create_static_tree, pre_order_traversal


def mirror_tree(node):
    """ Convert given tree into its mirror tree"""
    if node is not None:
        mirror_tree(node.left)
        mirror_tree(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp

    return node


if __name__ == '__main__':
    node = mirror_tree(create_static_tree())
    pre_order_traversal(node)
