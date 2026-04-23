from atds import *

def preorder(tree):
    if tree is None:
        return []
    return ([tree.get_root_val()] +
            preorder(tree.get_left_child()) +
            preorder(tree.get_right_child()))


def inorder(tree):
    if tree is None:
        return []
    return (inorder(tree.get_left_child()) +
            [tree.get_root_val()] +
            inorder(tree.get_right_child()))


def postorder(tree):
    if tree is None:
        return []
    return (postorder(tree.get_left_child()) +
            postorder(tree.get_right_child()) +
            [tree.get_root_val()])

def build_tree():
    a = BinaryTree('a')

    a.insert_left('b')
    a.insert_right('c')

    b = a.get_left_child()
    c = a.get_right_child()

    b.insert_left('d')
    b.insert_right('e')

    c.insert_left('f')
    c.insert_right('g')

    d = b.get_left_child()
    e = b.get_right_child()
    g = c.get_right_child()

    d.insert_left('h')
    d.insert_right('i')

    e.insert_right('j')

    g.insert_left('k')

    return a

def main():
    tree = build_tree()

    print("Preorder:", preorder(tree))
    print("Inorder:", inorder(tree))
    print("Postorder:", postorder(tree))


if __name__ == "__main__":
    main()