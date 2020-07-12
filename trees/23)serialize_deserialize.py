from trees.utils import Node, pre_order_traversal, create_static_tree


def serialize(node, arr):
    """ Serialization of binary tree. """
    if node is None:
        arr.append(None)
        return None
    arr.append(node.data)
    serialize(node.left, arr)
    serialize(node.right, arr)
    return arr


def deserialize(arr, i):
    """Deserialize the binary tree"""
    if arr[i[0]] is None:
        i[0] = i[0] + 1
        return None
    node = Node(arr[i[0]])
    i[0] = i[0] + 1
    node.left = deserialize(arr, i)
    node.right = deserialize(arr, i)
    return node


if __name__ == '__main__':

    arr = serialize(create_static_tree(), [])
    print(arr)
    node = deserialize(arr, [0])
    pre_order_traversal(node)
