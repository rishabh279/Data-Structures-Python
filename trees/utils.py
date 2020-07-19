class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree(parent_node=None, root_node=True):
    """ Creates a tree based on the user input """
    if root_node:
        root_data = input("Enter root node data ")
        parent_node = Node(root_data)
        create_tree(parent_node, False)
        return parent_node
    parent = parent_node
    left_child_presence = input("Enter 'y' if you want left child of " + str(parent.data) + " ")
    if left_child_presence == 'y':
        left_child_data = input("Enter left child data ")
        parent.left = Node(left_child_data)
        create_tree(parent.left, False)
    right_child_presence = input("Enter 'y' if you want right child of " + str(parent.data) + " ")
    if right_child_presence == 'y':
        right_child_data = input("Enter right child data ")
        parent.right = Node(right_child_data)
        create_tree(parent.right, False)


def create_static_tree():
    """ Create static tree. """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    #root.left.left.left = Node(8)
    #root.left.left.right = Node(9)
    root.left.right = Node(5)
    #root.left.right.left = Node(10)
    #root.left.right.right = Node(11)
    # root.left.right.right.left = Node(12)
    # root.left.right.right.left.left = Node(13)
    # root.left.right.right.left.left.left = Node(14)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root


def create_static_bst():
    """ Create static binary search tree. """
    root = Node(32)
    root.left = Node(16)
    root.right = Node(40)
    root.left.left = Node(14)
    root.left.right = Node(24)
    root.right.left = Node(37)
    root.right.right = Node(51)
    return root


def pre_order_traversal(root):
    """ Traversing tree in pre-order traversal. """
    print(root.data)
    if root.left is not None:
        pre_order_traversal(root.left)
    if root.right is not None:
        pre_order_traversal(root.right)


def in_order_traversal(root):
    """ Traversing tree in in-order traversal. """
    if root is None:
        return
    in_order_traversal(root.left)
    print(root.data)
    in_order_traversal(root.right)
# if __name__ == '__main__':
#     pre_order_traversal(create_static_tree())