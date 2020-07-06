from trees.utils import create_static_tree


def get_level_bt(node, key, level):
    """ Get the level of given key in binary tree """
    if node is None:
        return -1
    if node.data == key:
        return level

    temp = get_level_bt(node.left, key, level+1)

    if temp != -1:
        return temp

    return get_level_bt(node.right, key, level+1)


if __name__ == '__main__':
    print(get_level_bt(create_static_tree(), 3, 1))