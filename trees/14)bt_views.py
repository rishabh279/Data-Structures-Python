from trees.utils import Node


def left_view(node, level, max):
    """Print the left view of Binary Tree"""
    if node is None:
        return None

    if level > max[0]:
        print(node.data)
        max[0] = level
    left_view(node.left, level+1, max)
    left_view(node.right, level+1, max)


if __name__ == '__main__':
    root = Node(12)
    root.left = Node(10)
    root.right = Node(20)
    root.right.left = Node(25)
    root.right.right = Node(40)
    left_view(root, 1, [0])