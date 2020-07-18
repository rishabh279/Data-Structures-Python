from trees.utils import Node


def next_right_node(node, key):
    """ Finds the next right node of given node at """
    queue = []
    levels = []
    level = 1
    queue.append(node)
    levels.append(level)
    while len(queue) > 0:
        pop_node = queue.pop(0)
        pop_level = levels.pop(0)

        if pop_node.data == key:
            if len(queue) == 0 or pop_level != levels[0]:
                print("No right node to given key")
                return
            print(queue.pop(0).data)
            return 0

        if pop_node.left is not None:
            queue.append(pop_node.left)
            levels.append(pop_level + 1)
        if pop_node.right is not None:
            queue.append(pop_node.right)
            levels.append(pop_level + 1)

    print("No right node to given key")


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(6)
    root.right.right = Node(5)
    root.left.left = Node(8)
    root.left.right = Node(4)
    next_right_node(root, 8)





