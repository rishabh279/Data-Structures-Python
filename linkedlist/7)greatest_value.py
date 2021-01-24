class Node:
    def __init__(self, data):
        self.data = data
        self.arbitary = None
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, data):
        """ Insert node in linked list. """
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode

    def iterate(self):
        """ Iterate linked list. """
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def reverse(self):
        """ Reverse Linked List. """
        current = self.head
        prev = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev


def greatest_value(node):
    """ Greatest value node in linked list on its right side """
    max_elem = node.head.data
    max_node = node.head
    temp = node.head.next

    while temp:
        temp.arbitary = max_node
        if temp.data > max_elem:
            max_elem = temp.data
            max_node = temp
        temp = temp.next

    node.reverse()

    temp = node.head
    while temp:
        print(f'Element is {temp.data}')
        if temp.arbitary:
            print(f'Max is {temp.arbitary.data}')
        temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(5)
    ll.push(3)
    ll.push(10)
    ll.push(1)
    ll.reverse()
    greatest_value(ll)
    ll.reverse()
