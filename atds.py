class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class ULStack:

    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        return self.items.is_empty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop_at(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items.head.get_data()

    def size(self):
        return self.items.length()

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

class LinearSearcher:

    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return None
    
class BinarySearcher:

    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                low = mid + 1 
            else:
                high = mid - 1

        return None

class HashTable():
    
    def __init__(self, m):
        self.size = m
        self.slots = [None] * m
        self.data = [None] * m
        self.count = 0

    def __repr__(self):
        return "Keys:   " + str(self.slots) + "\nValues: " + str(self.data)

    def __len__(self):
        return self.count

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, value):
        hash_value = self.hash_function(key, self.size)
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
            self.count += 1
        elif self.slots[hash_value] == key:
            self.data[hash_value] = value
        else:
            next_slot = self.rehash(hash_value)
            while self.slots[next_slot] != None and self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot)
            if self.slots[next_slot] == None:
                self.slots[next_slot] = key
                self.data[next_slot] = value
                self.count += 1
            else:
                self.data[next_slot] = value

    def get(self, key):
        start_slot = self.hash_function(key, self.size)
        position = start_slot
        while self.slots[position] != None:
            if self.slots[position] == key:
                return self.data[position]
            position = self.rehash(position)
            if position == start_slot:
                return None
        return None
    
class BinaryTree:

    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def get_root_val(self):
        return self.key

    def set_root_val(self, new_val):
        self.key = new_val

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def insert_left(self, new_left_child):
        if self.left_child == None:
            self.left_child = BinaryTree(new_left_child)
        else:
            new_tree = BinaryTree(new_left_child)
            new_tree.left_child = self.left_child
            self.left_child = new_tree

    def insert_right(self, new_right_child):
        if self.right_child == None:
            self.right_child = BinaryTree(new_right_child)
        else:
            new_tree = BinaryTree(new_right_child)
            new_tree.right_child = self.right_child
            self.right_child = new_tree

    def __str__(self):
        return "BinaryTree[key=" + str(self.key) + ",left_child=" + str(self.left_child) + ",right_child=" + str(self.right_child) + "]"



class BinaryHeap():

    def __init__(self):
        self.heap_list = [0]

    def insert(self, value):
        self.heap_list.append(value)
        self.percolate_up(len(self.heap_list) - 1)

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[i // 2]
                self.heap_list[i // 2] = temp
            i = i // 2

    def del_min(self):
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[len(self.heap_list) - 1]
        self.heap_list.pop()
        if len(self.heap_list) > 1:
            self.percolate_down(1)

        return min_val

    def percolate_down(self, i):
        while (i * 2) < len(self.heap_list):
            min_child = self.min_child(i)

            if self.heap_list[i] > self.heap_list[min_child]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child]
                self.heap_list[min_child] = temp

            i = min_child

    def min_child(self, i):
        if i * 2 + 1 >= len(self.heap_list):
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def find_min(self):
        return self.heap_list[1]

    def is_empty(self):
        return len(self.heap_list) == 1

    def size(self):
        return len(self.heap_list) - 1

    def build_heap(self, list_of_keys):
        i = len(list_of_keys) // 2
        self.heap_list = [0] + list_of_keys[:]

        while i > 0:
            self.percolate_down(i)
            i = i - 1

    def __repr__(self):
        return "BinaryHeap" + str(self.heap_list)
    

class Vertex(object):
    """Describes a vertex object in terms of a "key" and a
    dictionary that indicates edges to neighboring vertices with
    a specified weight.
    """
    
    def __init__(self, key):
        """Constructs a vertex with a key value and an empty dictionary
        "connected_to" where we'll store other vertices to which this vertex is connected.
        """
        self.id = key
        self.connected_to = {}   # same idea as "neighbors" in notes

    def add_neighbor(self, neighbor_vertex, weight=0):
        """Adds a reference to a neighboring Vertex object to the dictionary."""
        self.connected_to[neighbor_vertex] = weight

    def __repr__(self):
        """Returns a representation of the vertex and its neighbors."""
        return str(self.id) + ' connected_to: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        """Returns the vertices we're connected to"""
        return self.connected_to.keys()

    def get_id(self):
        """Returns the id ("key") for this vertex"""
        return self.id

    def get_weight(self, neighbor_vertex):
        """Returns the weight of an edge connecting this vertex with another."""
        return self.connected_to[neighbor_vertex]
    

class Graph(object):
    """Describes the Graph class, which is primarily a dictionary  
    mapping vertex names to Vertex objects.
    """

    def __init__(self):
        """Initializes an empty dictionary of Vertex objects"""
        self.vertex_dict = {}

    def add_vertex(self, key):
        """Creates a new vertex and adds it to the graph"""
        new_vertex = Vertex(key)
        self.vertex_dict[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        """Returns the Vertex object if it exists, otherwise None"""
        return self.vertex_dict.get(key, None)

    def __contains__(self, key):
        """Allows 'key in graph' syntax"""
        return key in self.vertex_dict

    def add_edge(self, from_vertex, to_vertex, weight=0):
        """Adds an edge between two vertices"""
        # create vertices if they don't exist
        if from_vertex not in self.vertex_dict:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertex_dict:
            self.add_vertex(to_vertex)

        # connect them using Vertex method
        self.vertex_dict[from_vertex].add_neighbor(
            self.vertex_dict[to_vertex], weight
        )

    def get_vertices(self):
        """Returns all vertex keys"""
        return self.vertex_dict.keys()

    def __iter__(self):
        """Allows iteration over Vertex objects"""
        return iter(self.vertex_dict.values())