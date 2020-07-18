#other solution also available
from trees.utils import Node, pre_order_traversal


class LinkedList:
    def __init__(self, data):
        self.data = data
        self.right = None


def bt_from_linked_list(node, queue):
    """ Binary tree from linked list """
    root = Node(node.data)
    queue.append(root)
    while len(queue) > 0:
        pop_node = queue.pop(0)

        if node.right is not None:
            temp_node = Node(node.right.data)
            pop_node.left = temp_node
            queue.append(temp_node)
            node = node.right

        if node.right is not None:
            temp_node = Node(node.right.data)
            pop_node.right = temp_node
            queue.append(temp_node)
            node = node.right
    return root


if __name__ == '__main__':
    node = LinkedList(10)
    node.right = LinkedList(12)
    node.right.right = LinkedList(15)
    node.right.right.right = LinkedList(25)
    node.right.right.right.right = LinkedList(30)
    node.right.right.right.right.right = LinkedList(36)
    pre_order_traversal(bt_from_linked_list(node, []))
