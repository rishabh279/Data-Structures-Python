from linkedlist.utils import LinkedList


def detect_loop(node):
    """
    Detect loop in linked list
    """
    slow = node.head
    fast = node.head

    while fast is not None:
        if slow == fast:
            print(fast.data)
            return
        slow = slow.next
        fast = fast.next.next


if __name__ == '__main__':

    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)
    llist.head.next.next.next.next = llist.head

    detect_loop(llist)
