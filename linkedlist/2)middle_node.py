from linkedlist.utils import LinkedList


def middle_node(node):
    """
    Finding a middle node in linked list.
    """
    hash = {}
    count = 0
    while node is not None:
        hash[count] = node.data
        node = node.next
        count += 1

    print(hash[int(hash.__len__()/2)])


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    ll.push(40)
    ll.push(50)
    middle_node(ll.head)