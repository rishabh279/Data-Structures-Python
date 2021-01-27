from linkedlist.utils import LinkedList


def reverse(node):
    """ Reverse Linked List. """
    current = node
    prev = None

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    node = prev
    return node


def palindrome(node):
    """Check whether given linked list is palindrome or not"""
    ll_count = 0
    temp = node.head
    while temp:
        ll_count += 1
        temp = temp.next

    ll_mid = int(ll_count / 2)

    temp = node.head
    ll_mid_temp = ll_mid
    while ll_mid_temp > 0:
        ll_mid_temp -= 1
        temp = temp.next

    mid_node = temp
    reverse_node = reverse(mid_node)
    temp = node.head
    ll_mid_temp = ll_mid
    while ll_mid_temp > 0:
        if temp.data != reverse_node.data:
            print('Not Palindrome')
            return
        temp = temp.next
        reverse_node = reverse_node.next

        ll_mid_temp -= 1
    print('Palindrome')


if __name__ == '__main__':
    node = LinkedList()
    node.push(2)
    node.push(4)
    node.push(5)
    node.push(4)
    node.push(2)
    node.push(1)
    palindrome(node)