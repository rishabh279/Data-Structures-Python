class Node:
    def __init__(self, data):
        self.data = data
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


# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.push(10)
#     ll.push(20)
#     ll.push(30)
#     ll.push(40)
#     ll.iterate()