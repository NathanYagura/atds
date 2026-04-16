#!/usr/bin/env python3
"""
parse_tree.py
Parses mathematical expressions from fully-parenthesized strings.
"""

__author__ = "Nathan Yagura"
__version__ = "2026-04-15"

from atds import Stack, BinaryTree


def build_parse_tree(fpexpr):
    """Creates a binary tree from the fully-parenthesized
    expression. We'll do this by pushing the current tree
    (current_focus) onto a stack when we descend to its 
    subtree to edit that subtree), then pop the stack
    to get back to previous parent trees when we've completed
    filling out the subtree.
    """
    
    tokens = fpexpr.split()

    pt = BinaryTree("")
    stack = Stack()
    stack.push(pt)

    current_focus = pt

    for token in tokens:

        if token == "(":
            current_focus.insert_left("")
            stack.push(current_focus)
            current_focus = current_focus.get_left_child()

        elif token in "+-*/":
            current_focus.set_root_val(token)
            current_focus.insert_right("")
            stack.push(current_focus)
            current_focus = current_focus.get_right_child()

        elif token == ")":
            current_focus = stack.pop()

        else:
            current_focus.set_root_val(int(token))
            current_focus = stack.pop()

    return pt


def evaluate(parse_tree):
    
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    if left is None and right is None:
        return parse_tree.get_root_val()

    if parse_tree.get_root_val() == "+":
        return evaluate(left) + evaluate(right)
    elif parse_tree.get_root_val() == "-":
        return evaluate(left) - evaluate(right)
    elif parse_tree.get_root_val() == "*":
        return evaluate(left) * evaluate(right)
    elif parse_tree.get_root_val() == "/":
        return evaluate(left) / evaluate(right)


def main():
    EPSILON = 0.001
    tests = [("( 2 + 3 )", 5)]

    for i in range(len(tests)):
        print("Testing expression", tests[i][0])
        pt = build_parse_tree(tests[i][0])
        print("Result:", evaluate(pt))
        if abs(evaluate(pt) - tests[i][1]) < EPSILON:
            print("Test", i + 1, "passed")
        else:
            print("Test", i + 1, "failed")

    print("""Test 6 should fail. It's an attempt to calculate pi that doesn't 
get very far.""")


if __name__ == "__main__":
    main()