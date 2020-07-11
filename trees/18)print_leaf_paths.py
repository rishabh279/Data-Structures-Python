from trees.utils import create_static_tree


def get_leaf_path(node, pathlen, path):
    """ Print the root to leaf paths in binary tree"""
    if node is not None:
        if len(path) > pathlen:
            path[pathlen] = node.data
        else:
            path.append(node.data)
        pathlen = pathlen + 1

    if node.left is None and node.right is None:
        print(path[0:pathlen])
    else:
        get_leaf_path(node.left, pathlen, path)
        get_leaf_path(node.right, pathlen, path)


if __name__ == '__main__':
    get_leaf_path(create_static_tree(), 0, [])