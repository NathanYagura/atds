"""
I compared the performance of two implementations of the Stack
abstract data type in this program (Stack - uses Python list, and ULStack - uses
UnorderedList). I measured the time it took to perform push() and pop() operations for each implementation.

Based off the results, I could tell that list-based Stack was faster for
push and pop operations. This is probably because Python lists are optimized for
append() and pop() at the end of the list. In contrast, the UnorderedList implementation requires traversing
nodes or updating links between them. This is probably what makes it slower than Stack.

The ULStack also relies on linked list operations like add() and
pop_at() which involve pointer manipulation and are not as efficient than direct
index access in lists.

The list-based Stack performs better because it uses built-in data
structures that are highly optimized while the UnorderedList-based stack
requires more complex operations that take longer time in general.
"""

import time
from atds import Stack, ULStack


def test_push(stack, n):
    start = time.time()
    for i in range(n):
        stack.push(i)
    end = time.time()
    return end - start


def test_pop(stack, n):
    start = time.time()
    for i in range(n):
        stack.pop()
    end = time.time()
    return end - start


def main():
    n = 10000  # number of operations

    # Test list-based stack
    s1 = Stack()
    push_time_1 = test_push(s1, n)
    pop_time_1 = test_pop(s1, n)

    # Test unordered list stack
    s2 = ULStack()
    push_time_2 = test_push(s2, n)
    pop_time_2 = test_pop(s2, n)

    print("Results for", n, "operations:\n")

    print("List-based Stack:")
    print("Push time:", push_time_1)
    print("Pop time:", pop_time_1)

    print("\nUnorderedList-based Stack:")
    print("Push time:", push_time_2)
    print("Pop time:", pop_time_2)


if __name__ == "__main__":
    main()