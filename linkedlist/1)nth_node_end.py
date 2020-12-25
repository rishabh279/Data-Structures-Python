from linkedlist.utils import LinkedList


def nth_node_from_end(node, n):
    """
    Find n’th node from the end of a Linked List.
    """
    slow = node.head
    fast = node.head
    i = n - 1
    while i > 0:
        fast = fast.next
        i = i - 1
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    print(slow.data)


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(35)
    nth_node_from_end(llist, 2)