from linkedlist.utils import LinkedList


def alternating_split(node):
    """ Alternating split of a given linked list. """
    first_list = node.head
    second_list = node.head.next
    p = node.head
    while p.next:
        temp = p.next
        p.next = p.next.next
        p = temp

    print(f'First List')
    while first_list:
        print(first_list.data)
        first_list = first_list.next

    print(f'Second List')
    while second_list:
        print(second_list.data)
        second_list = second_list.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    ll.push(40)
    ll.push(50)

    alternating_split(ll)

