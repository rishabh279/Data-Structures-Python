from trees.utils import Node


def evaluate_expression_tree(node):
    """ Evaluate the given expression binary tree"""
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return node.data

    left_exp = evaluate_expression_tree(node.left)
    right_exp = evaluate_expression_tree(node.right)

    if node.data == '+':
        return left_exp + right_exp

    if node.data == '-':
        return left_exp - right_exp

    if node.data == '*':
        return left_exp * right_exp

    if node.data == '/':
        return left_exp / right_exp


if __name__ == '__main__':
    root = Node('+')
    root.left = Node('*')
    root.left.left = Node(5)
    root.left.right = Node(4)
    root.right = Node('-')
    root.right.left = Node(100)
    root.right.right = Node(20)
    print(evaluate_expression_tree(root))
