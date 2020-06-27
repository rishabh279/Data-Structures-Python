from trees.utils import create_static_tree


class Height:
    def __init__(self):
        self.h = 0


def height(node):
    """Find the height of the tree. """
    if node is None:
        return 0
    else:
        left = height(node.left)
        right = height(node.right)

        return 1 + max(left, right)


def diameter_approach1(node):
    """ Calculate the diameter of the tree in O(n^2) """
    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    left_diameter = diameter_approach1(node.left)
    right_diameter = diameter_approach1(node.right)

    return max(1 + left_height + right_height, max(left_diameter, right_diameter))


def diameter_approach2(node, height):
    """ Calculate the diameter of tree in O(n) """
    lh = Height()
    rh = Height()

    if node is None:
        height.h = 0
        return 0

    left_diameter = diameter_approach2(node.left, lh)
    right_diameter = diameter_approach2(node.right, rh)

    height.h = 1 + max(lh.h, rh.h)

    return max(lh.h + rh.h + 1, max(left_diameter, right_diameter))


if __name__ == '__main__':
    # print(height(create_static_tree()))
    print(diameter_approach1(create_static_tree()))
    print(diameter_approach2(create_static_tree(), Height()))

