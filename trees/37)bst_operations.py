from trees.utils import Node, pre_order_traversal


def search_node(node, key):
    """search node in a given binary tree"""
    if node is None:
        print('Node is not present in the tree')
        return None
    if key > node.data:
        search_node(node.right, key)
    elif key < node.data:
        search_node(node.left, key)
    elif node.data == key:
        print('Node is present in the tree')
        return node


def insert_node(node, key):
    """Insert node in the given binary tree"""
    if key > node.data:
        if node.right is None:
            newnode = Node(key)
            node.right = newnode
        else:
            insert_node(node.right, key)
    elif key < node.data:
        if node.left is None:
            newnode = Node(key)
            node.left = newnode
        else:
            insert_node(node.left, key)


def min_value_node(node):
    """ Find min value in given bst subtree"""
    current = node

    while current.left is not None:
        current = current.left

    return current


def delete_node(root, key):
    """Delete given node from BST"""
    if root is None:
        return root

    if key < root.data:
        root.left = delete_node(root.left, key)

    elif (key > root.data):
        root.right = delete_node(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            return temp

        elif root.right is None:
            temp = root.left
            return temp

        temp = min_value_node(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)

    return root


if __name__ == '__main__':
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)
    #insert_node(root, 90)
    #search(root, 80)
    delete_node(root, 20)
    pre_order_traversal(root)