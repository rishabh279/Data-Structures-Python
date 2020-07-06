#ref: https://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_nodes(node, d, i):
    """ Print nodes after d-distance """
    if node is None:
        return -1
    if d == i:
        print(node.data)
        return
    print_nodes(node.left, d, i+1)
    print_nodes(node.right, d, i+1)


def print_k_nodes(node, target, d):
    if node is None:
        return -1
    if node == target:
        print_nodes(node, d, 0)
        return 1
    dl = print_k_nodes(node.left, target, d)
    if dl != -1:
        if dl == d:
            print(node.data)
        else:
            print_nodes(node.right, d-dl-1, 0)
        return dl + 1
    dr = print_k_nodes(node.right, target, d)
    if dr != -1:
        if dr == d:
            print(node.data)
        else:
            print_nodes(node.left, d - dr - 1, 0)
        return dr + 1
    return -1


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    target = root.left.left
    print_k_nodes(root, target, 3)