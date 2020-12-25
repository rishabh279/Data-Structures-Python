from linkedlist.utils import LinkedList


def intersection_point(node1, node2):
    """
    Intersect point of two single linked lists.
    """
    count1 = 0
    count2 = 0
    current = node1
    while current is not None:
        count1 += 1
        current = current.next

    current = node2
    while current is not None:
        count2 += 1
        current = current.next

    if count1 > count2:
        big_ll = node1
        small_ll = node2
    else:
        big_ll = node2
        small_ll = node1

    diff = abs(count1 - count2)

    while diff > 0:
        big_ll = big_ll.next
        diff -= 1

    while big_ll.next is not None:
        if big_ll.data == small_ll.data:
            print(big_ll.data)
        big_ll = big_ll.next
        small_ll = small_ll.next


if __name__ == '__main__':
    node1 = LinkedList()
    node1.push(3)
    node1.push(6)
    node1.push(9)
    node1.push(15)
    node1.push(30)

    node2 = LinkedList()
    node2.push(10)
    node2.push(15)
    node2.push(30)

    intersection_point(node1.head, node2.head)