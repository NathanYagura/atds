#!/usr/bin/env/ python3
"""
create_this_tree.py
Write a main program to create each of the trees given here.
This program prints out expected results based on a __str__() or __repr__() method 
being availabe for the BinaryTree class.
"""

from atds import BinaryTree

def main():
    print('''
    bt1:
                           A
                         /   \\
                        B     C
                      /
                     D
        ''')
    print('''Expected result, bt1:
    BinaryTree[key=A,
    left_child=BinaryTree[key=B,
    left_child=BinaryTree[key=D,
    left_child=None,
    right_child=None],
    right_child=None],
    right_child=BinaryTree[key=C,
    left_child=None,
    right_child=None]]''')
    print('--------------------')
    print("Example Solution")
    print('My result:')
    bt1 = BinaryTree('A')
    bt1.insertRight('C')
    bt1.insertLeft('D')
    bt1.insertLeft('B')
    print(bt1)
    print('--------------------')
    # Another way of doing the same tree
    bt1a = BinaryTree('A')
    bt1a.insertLeft('B')
    bt1a.getLeftChild().insertLeft('D')
    bt1a.insertRight('C')
    print(bt1a)
    print('--------------------')
    print('''
    bt2:
                            A
                          /   \\
                         /     \\
                        B       C
                         \\     / \\
                          D   E   F
    ''')
    print('''Expected result bt2:
    BinaryTree[key=A,
    left_child=BinaryTree[key=B,
    left_child=None,
    right_child=BinaryTree[key=D,
    left_child=None,
    right_child=None]],
    right_child=BinaryTree[key=C,
    left_child=BinaryTree[key=E,
    left_child=None,
    right_child=None],
    right_child=BinaryTree[key=F,
    left_child=None,
    right_child=None]]]''')
    print('--------------------')
    print('My result:')











    print('--------------------')
    print('''
    bt3:
                            A
                              \\
                                B
                               / 
                             C
                            / \\ 
                          D    E
    ''')

    print('''Expected result bt3:
    BinaryTree[key=A,
    left_child=None,
    right_child=BinaryTree[key=B,
    left_child=BinaryTree[key=C,
    left_child=BinaryTree[key=D,
    left_child=None,
    right_child=None],
    right_child=BinaryTree[key=E,
    left_child=None,
    right_child=None]],
    right_child=None]]''')
    print('--------------------')
    print('My result:')










    print('--------------------')
    print('''
    bt4:
                            A
                          /   \\
                        /       \\
                      /           \\
                    B               C
                  /   \\           /   \\
                /       \\       /       \\
              D           E   F           G
            /   \\       /
           H      I    J
    ''')

    print('''Expected result bt4:
    BinaryTree[key=A,
    left_child=BinaryTree[key=B,
    left_child=BinaryTree[key=D,
    left_child=BinaryTree[key=H,
    left_child=None,
    right_child=None],
    right_child=BinaryTree[key=I,
    left_child=None,
    right_child=None]],
    right_child=BinaryTree[key=E,
    left_child=BinaryTree[key=J,
    left_child=None,
    right_child=None],
    right_child=None]],
    right_child=BinaryTree[key=C,
    left_child=BinaryTree[key=F,
    left_child=None,
    right_child=None],
    right_child=BinaryTree[key=G,
    left_child=None,
    right_child=None]]]''')
    print('--------------------')
    print('My result:')
    
    
    
    
    
    
    
    
    
    
    
    print('--------------------')
    


main()


