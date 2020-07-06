#ref https://www.ideserve.co.in/learn/construct-binary-tree-from-inorder-and-preorder-traversals
from trees.utils import Node, pre_order_traversal


def search_index(inorder, elem):
    for i in range(len(inorder)):
        if inorder[i] == elem:
            break
    return i


def build_tree_approach_1(inorder, instart, inend, postorder, pstart, pend):
    if instart > inend or pstart > pend:
        return None

    node = Node(postorder[pstart])

    index = search_index(inorder, postorder[pstart])
    lefttreesize = index - instart
    righttreesize = inend - index

    node.left = build_tree_approach_1(inorder, instart, index-1, postorder, pstart+1, pstart+lefttreesize)
    node.right = build_tree_approach_1(inorder, index+1, inend, postorder, pstart+lefttreesize+1, pstart+lefttreesize+righttreesize)

    return node


def build_tree_approach_2():
    pass


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    node = build_tree_approach_1(inorder, 0, len(inorder)-1, preorder, 0, len(preorder)-1)
    pre_order_traversal(node)