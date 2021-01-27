from linkedlist.utils import Node


def start_node(node):
    """ Find the starting node of cycle if cycle exists in a given linked list. """
    slow = node
    fast = node

    intersect_node = None
    while fast and slow and fast.next:

        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next

    print(slow.data)
    print(fast.data)


if __name__ == '__main__':
    head = Node(50)
    head.next = Node(20)
    head.next.next = Node(15)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(10)

    # Create a loop for testing
    head.next.next.next.next.next = head.next.next

    start_node(head)