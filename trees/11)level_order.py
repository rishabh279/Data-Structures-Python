from trees.utils import create_static_tree


def level_order_traversal(node):
    """ Traverse the tree in level order. """
    if node is None:
        return None
    queue = []
    queue.append(node)
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.data)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


if __name__ == '__main__':
    level_order_traversal(create_static_tree())
