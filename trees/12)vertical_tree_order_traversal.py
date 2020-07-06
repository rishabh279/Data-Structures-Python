from trees.utils import create_static_tree, Node


class LLnode:
    def __init__(self):
        self.data = []
        self.left = None
        self.right = None


def find_size(node, tl, max, min):
    """ Find min and max horizontal distance of Binary Tree. """
    if node is None:
        return None
    if tl < min[0]:
        min[0] = tl
    if tl > max[0]:
        max[0] = tl
    find_size(node.left, tl-1, max, min)
    find_size(node.right, tl+1, max, min)
    return max, min


def vertical_traversal_approach_1(node, vertical_distance, temp):
    """ Prints the elements of binary tree in vertical order traversal approach1 """
    if node is None:
        return
    if vertical_distance == temp:
        print(node.data)
    vertical_traversal_approach_1(node.left, vertical_distance, temp-1)
    vertical_traversal_approach_1(node.right, vertical_distance, temp+1)


def vertical_traversal_approach_2(node, temp, dict):
    """ Prints the elements of binary tree in vertical order traversal using HashMap """
    if node is None:
        return None
    dict[node.data] = temp
    vertical_traversal_approach_2(node.left, temp-1, dict)
    vertical_traversal_approach_2(node.right, temp+1, dict)


def vertical_traversal_approach_3(node, llnode):
    """ Prints the elements of binary tree in vertical order traversal using DoubleLinkedList """
    if node is None:
        return None
    llnode.data.append(node.data)

    if node.left is not None:
        if llnode.left is None:
            new_llnode = LLnode()
            llnode.left = new_llnode
            new_llnode.right = llnode
        vertical_traversal_approach_3(node.left, llnode.left)

    if node.right is not None:
        if llnode.right is None:
            new_llnode = LLnode()
            llnode.right = new_llnode
            new_llnode.left = llnode
        vertical_traversal_approach_3(node.right, llnode.right)


if __name__ == '__main__':
    ## approach1
    # max, min = find_size(create_static_tree(), 0, [0], [0])
    # for i in range(min[0], max[0]+1):
    #     vertical_traversal_approach_1(create_static_tree(), i, 0)

    ##approach2
    # dict = {}
    # vertical_traversal_approach_2(create_static_tree(), 0, dict)
    # max_horizontal_key = max(dict, key=lambda x: dict[x])
    # min_horizontal_key = min(dict, key=lambda x: dict[x])
    #
    # max_horizontal = dict[max_horizontal_key]
    # min_horizontal = dict[min_horizontal_key]
    # sorted_distance = sorted(dict.items(), key=lambda x: x[1])
    # for key, value in sorted_distance:
    #     print(key)

    ## approach3
    llnode = LLnode()
    vertical_traversal_approach_3(create_static_tree(), llnode)
    while llnode.left is not None:
        llnode = llnode.left
    while llnode.right is not None:
        print(llnode.data)
        llnode = llnode.right