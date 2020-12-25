from linkedlist.utils import LinkedList


def reverse(node):
    """ Reverse Linked List. """
    current = node.head
    prev = None

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    node.head = prev
    temp = node.head
    while temp is not None:
        print(temp.data)
        temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    ll.push(40)
    ll.push(50)
    reverse(ll)
