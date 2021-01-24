from linkedlist.utils import LinkedList, Node


def merge_sorted_linked_list(node1, node2):
    """Merge two sorted linked lists into one sorted linked list"""
    temp_head = Node(0)
    node1 = node1.head
    node2 = node2.head
    temp = temp_head

    while node1 and node2:
        if node1.data < node2.data:
            temp.next = node1
            node1 = node1.next
        elif node2.data < node1.data:
            temp.next = node2
            node2 = node2.next
        temp = temp.next

    while node1:
        temp.next = node1
        temp = temp.next
        node1 = node1.next

    while node2:
        temp.next = node2
        temp = temp.next
        node2 = node2.next

    iter = temp_head.next
    while iter:
        print(iter.data)
        iter = iter.next


if __name__ == '__main__':
    node1 = LinkedList()
    node1.push(2)
    node1.push(4)
    node1.push(5)

    node2 = LinkedList()
    node2.push(1)
    node2.push(6)
    node2.push(8)

    merge_sorted_linked_list(node1, node2)