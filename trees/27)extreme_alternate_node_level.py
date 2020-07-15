from trees.utils import Node


def print_extreme_node(node):
    """ Print extreme alternative node in given binary tree"""
    queue = []
    queue.append(node)
    flag = False
    while len(queue) > 0:
        count_node = len(queue)
        i = 0
        while i < count_node:
            if queue[0].left is not None:
                queue.append(queue[0].left)
            if queue[0].right is not None:
                queue.append(queue[0].right)
            pop_node = queue.pop(0)
            if not flag and i == 0:
                print(pop_node.data)
            elif flag and i == count_node-1:
                print(pop_node.data)
            i = i + 1
        flag = not flag


if __name__ == '__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)

    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    root.left.left.left.left = Node(16)
    root.left.left.left.right = Node(17)
    root.right.right.right.right = Node(31)

    print_extreme_node(root)
