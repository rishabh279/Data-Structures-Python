from trees.utils import Node, in_order_traversal


def bst_array(node, arr):
    """ Convert given bst to array"""
    if node is None:
        return
    bst_array(node.left, arr)
    arr.append(node)
    bst_array(node.right, arr)
    return arr


def array_balanced_bst(arr, start, end):
    """ Convert given array of nodes to balanced BST """
    if start > end:
        return
    mid = int((start+end)/2)
    node = arr[mid]

    node.left = array_balanced_bst(arr, start, mid-1)
    node.right = array_balanced_bst(arr, mid+1, end)
    return node


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(7)
    root.left.left.left = Node(6)
    root.left.left.left.left = Node(5)

    arr = bst_array(root, [])
    node = array_balanced_bst(arr, 0, len(arr)-1)
    in_order_traversal(node)