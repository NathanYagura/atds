
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        if len(self.item) > 0:
            self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0
    
class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def length(self):
        node_count = 0
        current = self.head
        while current != None:
            node_count += 1
            current = current.get_next()
        return node_count

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        previous = None
        current = self.head
        while current != None:
            if current.get_data() == item:
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                return
            else:
                previous = current
                current = current.get_next()

    def append(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(temp)

    def index(self, item):
        current = self.head
        position = 0
        while current != None:
            if current.get_data() == item:
                return position
            current = current.get_next()
            position += 1

    def insert(self, pos, item):
        temp = Node(item)
        if pos == 0:
            temp.set_next(self.head)
            self.head = temp
        else:
            current = self.head
            previous = None
            position = 0
            while position < pos:
                previous = current
                current = current.get_next()
                position += 1
            temp.set_next(current)
            previous.set_next(temp)

    def pop(self):
        current = self.head
        previous = None

        if current == None:
            return None

        while current.get_next() != None:
            previous = current
            current = current.get_next()

        if previous == None:
            self.head = None
        else:
            previous.set_next(None)

        return current.get_data()


    def pop_at(self, pos):
        current = self.head
        previous = None
        position = 0

        while position < pos:
            previous = current
            current = current.get_next()
            position += 1

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return current.get_data()

    def __repr__(self):
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result

