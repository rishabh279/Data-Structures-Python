from linkedlist.utils import LinkedList, Node


def sort_0_1_2(node):
    """ Sort a linked list of 0_s 1_s and 2_s. """
    if node.head == None or node.head.next == None:
        return node
    zero_elem = Node(0)
    one_elem = Node(0)
    two_elem = Node(0)

    zero = zero_elem
    one = one_elem
    two = two_elem

    curr = node.head
    while curr:
        if curr.data == 0:
            zero.next = curr
            zero = zero.next
        elif curr.data == 1:
            one.next = curr
            one = one.next
        else:
            two.next = curr
            two = two.next
        curr = curr.next

    zero.next = one_elem.next if one_elem.next else two_elem.next
    one.next = two_elem.next
    two.next = None

    node.head = zero_elem.next

    return node
           

if __name__ == '__main__':
    ll = LinkedList()
    ll.push(2)
    ll.push(0)
    ll.push(2)
    ll.push(1)
    ll.push(2)
    ll.push(0)
    sort_0_1_2(ll)
    ll.iterate()