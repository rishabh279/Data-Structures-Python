from trees.utils import Node


def product_sum(stack1,stack2, node, product):
    """ Product of sum at same level in binary tree """
    sum = 0
    while len(stack1) > 0:
        node = stack1.pop(0)
        sum += node.data
        if node.left is not None:
            stack2.append(node.left)
        if node.right is not None:
            stack2.append(node.right)

    if sum != 0:
        product = product * sum

    sum = 0
    while len(stack2) > 0:
        node = stack2.pop(0)
        sum += node.data
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)

    if sum != 0:
        product = product * sum

    if len(stack2) == 0 and len(stack1) == 0:
        print(product)

    if len(stack1) > 0 or len(stack2) > 0:
        return product_sum(stack1, stack2, node, product)


if __name__ == '__main__':
    stack1 = []
    stack2 = []
    product = 1

    root = Node(2)
    stack1.append(root)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.left = Node(8)

    product_sum(stack1, stack2, root, 1)