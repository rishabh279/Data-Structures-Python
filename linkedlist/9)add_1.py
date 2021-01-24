from linkedlist.utils import LinkedList, Node


def add_one(node):
    """ Add 1 to number represented in linked list. """
    node.reverse()
    head = node.head
    carry = 1

    while head:
        sum = carry + head.data
        if sum % 10 == 0:
            carry = 1
            sum = sum % 10
        else:
            carry = 0

        head.data = sum
        temp = head
        head = head.next

    if carry > 0:
        temp.next = Node(carry)

    node.reverse()

    temp = node.head
    while temp:
        print(temp.data)
        temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(9)
    ll.push(5)
    ll.push(9)
    ll.push(9)
    ll.push(9)

    add_one(ll)
