#!/usr/bin/env python3
"""
stack_tester.py
Demonstrates the use of the Stack class.
@author Richard White
@version 2016-12-17
"""

from atds import Stack

def main():
    print("Testing the Stack class")
    testsPassed = 0


    try:
        s = Stack()
        testsPassed += 1
        print("Test passed: stack created")
    except:
        print("Test failed: couldn't initialize stack")

    try:
        s.push("hello")
        s.push(3)
        testsPassed += 1
        print("Test passed: items pushed")
    except:
        print("Test failed: couldn't push onto stack")

    try:
        result = s.peek()
        if (result == 3):
            testsPassed += 1
            print("Test passed: peeked at item")
        else:
            print("Test failed: incorrect peek value")
    except: 
        print("Test failed: couldn't peek at stack")

    try:
        result = s.pop()
        if (result == 3):
            testsPassed += 1
            print("Test passed: item popped")
        else:
            print("Test failed: incorrect pop result")
    except:
        print("Test failed: couldn't pop")

    try:
        result = s.is_empty()
        if (not result):
            testsPassed += 1
            print("Test passed: is_empty returned correct result")
        else:
            print("Test failed: stack has items, but indicated empty")
    except:
        print("Test failed: is_empty() method unavailable")

    try:
        result = s.size()
        if (result == 1):
            testsPassed += 1
            print("Test passed: correct size returned")
        else:
            print("Test failed: incorrect size returned")
    except:
        print("Test failed: size() method unavailable")

    try:
        s.pop()
    except:
        pass

    try:
        result = s.is_empty()
        if (result):
            testsPassed += 1
            print("Test passed: .is_empty() correctly indicating empty status")
        else:
            print("Test failed: stack failed to indicate empty status")
    except:
        print("Test failed: is_empty() unavailable")

    print(str(testsPassed) + "/7 tests passed")

if __name__ == "__main__":
    main()
