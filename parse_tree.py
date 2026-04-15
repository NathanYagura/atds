#!/usr/bin/env python3
"""
parse_tree.py
Parses mathematical expressions from fully-parenthesized strings.
"""

__author__ = "Nathan Yagura"
__version__ = "2026-04-15"

from atds import Stack, BinaryTree


def build_parse_tree(fpexpr):
    """Build parse tree using rules from notes."""
    
    tokens = fpexpr.split()

    pt = BinaryTree("")
    stack = Stack()
    stack.push(pt)

    current_focus = pt

    for token in tokens:

        if token == "(":
            # add left child and go down
            current_focus.insert_left("")
            stack.push(current_focus)
            current_focus = current_focus.get_left_child()

        elif token in "+-*/":
            # set operator, go right
            current_focus.set_root_val(token)
            current_focus.insert_right("")
            stack.push(current_focus)
            current_focus = current_focus.get_right_child()

        elif token == ")":
            # go up to parent
            current_focus = stack.pop()

        else:
            # operand: set value and go up
            current_focus.set_root_val(int(token))
            current_focus = stack.pop()

    return pt


def evaluate(parse_tree):
    """Evaluate using recursive strategy from notes."""
    
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    # base case: leaf node
    if left is None and right is None:
        return parse_tree.get_root_val()

    # recursive case
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