class Node:
    def __init__(self, data):
        self.child = []
        self.data = data


def serialize_nary(node, arr):
    """ Serialize the binary tree """
    arr.append(node.data)
    for chld in node.child:
        if chld is not None:
            serialize_nary(chld, arr)
    arr.append('p')
    return arr


def deserialize_nary(arr, i):
    """ Deserialize the binary tree """
    if arr[i[0]] == 'p':
        i[0] = i[0] + 1
        return
    node = Node(arr[i[0]])
    i[0] = i[0] + 1
    #while i[0] < len(arr):
    node.child.append(deserialize_nary(arr, i))
    #return node


if __name__ == '__main__':
    node = Node(1)
    node.child.append(Node(2))
    node.child.append(Node(3))
    # node.child.append(Node(4))
    # node.child[0].child.append(Node(5))
    arr = serialize_nary(node, [])
    print(arr)
    root = deserialize_nary(arr, [0])
    print(serialize_nary(root, []))