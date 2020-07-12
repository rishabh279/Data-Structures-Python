from trees.utils import create_static_tree


def sprial_traversal(stack1, stack2):
    """ Print tree in level order traversal in spiral form """
    while len(stack1) != 0:
        node = stack1.pop()
        print(node.data)
        if node.right is not None:
            stack2.append(node.right)
        if node.left is not None:
            stack2.append(node.left)

    while len(stack2) != 0:
        node = stack2.pop()
        print(node.data)
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)

    if len(stack2) > 0 or len(stack1) > 0:
        sprial_traversal(stack1, stack2)


if __name__ == '__main__':
    root = create_static_tree()
    stack1 = []
    stack2 = []
    stack1.append(root)
    sprial_traversal(stack1, stack2)



