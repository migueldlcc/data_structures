class Stack:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.size() == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        value = self.items[self.size() - 1]
        del self.items[-1]
        return value
    def peek(self):
        return self.items[self.size() - 1]

class Deque:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def append(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def appendLeft(self, item):
        self.items.insert(0, item)
    def popLeft(self):
        return self.items.pop(0)
    def extend(self, iterable):
        self.items.extend(iterable)
    def extendLeft(self, iterable):
        rev = list(iterable)
        rev.reverse()
        rev.extend(self.items)
        self.items = rev
    def rotate(self, n):
        if n > 0:
            for i in range(n):
                self.appendLeft(self.pop())
        else:
            for i in range(n * -1):
                self.append(self.popLeft())
    # Extended methods
    def __str__(self):
        return str(self.items)
    def peek(self):
        return self.items[self.size() - 1]
    def peekLeft(self):
        return self.items[0]


class Queue:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.size() == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.size() > 0:
            return self.items.pop(0)
        else:
            raise Exception("Cannot call dequeue() on an empty queue.")
    def peek(self):
        if self.size() > 0:
            return self.items[0]
        else:
            return None
    def clear(self):
        self.items = []
    def __str__(self):
        return str(self.items)
    def __add__(self, iterable):
        self.items.extend(iterable)
        return self

class Node:
    def __init__(self, *initdata):
        self.next = None
        if len(initdata) > 0:
            self.data = initdata[0]
        else:
            self.data = None
    def setData(self, newdata):
        self.data = newdata;
    def getData(self):
        return self.data
    def setNext(self, other):
        self.next = other
    def getNext(self):
        return self.next

class LinkedList:
    def __init__(self, *initnode):
        self.head = None
        if len(initnode) > 0:
            if isinstance(initnode[0], Node):
                self.head = initnode[0]
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        if isinstance(item, Node):
            temp = item
        else:
            temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def __str__(self):
        current = self.head
        output = []
        while current != None:
            output.append(current.getData())
            current = current.getNext()
        return str(output)
    def search(self, value):
        current = self.head
        while current != None:
            if current.getData() == value:
                return True
            current = current.getNext()
        return False
    def remove(self, value):
        while self.head.getData() == value:
            self.head = self.head.getNext()
        current = self.head
        while current != None: 
            while current.getNext() != None and current.getNext().getData() == value:
                current.setNext(current.getNext().getNext())
            current = current.getNext()
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    # Implements the len() function. Example: i = len(myLinkedList)
    def __len__(self):
        return self.length()
    # Implements the += operator. Example: myLinkedList += "New Value"
    def __iadd__(self, item):
        self.add(item)
        return self
    # Implements the in operator. Example: if "Some Value" in myLinkedList:
    def __contains__(self, value):
        return self.search(value)

class OrderedList:
    def __init__(self, *initnode):
        self.head = None
        if len(initnode) > 0:
            if isinstance(initnode[0], Node):
                self.head = initnode[0]
    def isEmpty(self):
        return self.head == None
    def __str__(self):
        current = self.head
        output = []
        while current != None:
            output.append(current.getData())
            current = current.getNext()
        return str(output)
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    def __len__(self):
        return self.length()
    def __iadd__(self, item):
        self.add(item)
        return self
    def __contains__(self, value):
        return self.search(value)

    # search() is the same as LinkedList.search with 1 adjustment.
    def search(self, value):
        current = self.head
        while current != None:
            if current.getData() == value:
                return True
            if current.getData() > value:
                return False
            current = current.getNext()
        return False

    # remove() is the same as LinkedList.remove with 1 adjustment.
    def remove(self, value):
        while self.head.getData() == value:
            self.head = self.head.getNext()
        current = self.head
        while current != None:
            while current.getNext() != None and current.getNext().getData() == value:
                current.setNext(current.getNext().getNext())
            if current.getData() > value:
                break
            else:
                current = current.getNext()

    # add() is considerably different from LinkedList.add.
    def add(self, item):
        if isinstance(item, Node):
            newNode = item
        else:
            newNode = Node(item)
        if self.head == None or self.head.getData() > newNode.getData():
            newNode.setNext(self.head)
            self.head = newNode
        else:
            prevNode = None
            curNode = self.head
            while curNode != None:
                if curNode.getData() > newNode.getData():
                    break
                else:
                    prevNode = curNode
                    curNode = curNode.getNext()
            newNode.setNext(curNode)
            prevNode.setNext(newNode)

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.parent = None
        self.leftChild = None
        self.rightChild = None

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
        self.leftChild.parent = self
        return self.leftChild

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.leftChild
            self.rightChild = t
        self.rightChild.parent = self
        return self.rightChild

    # CHANGES -----------------------------------------------------------
    def children(self):
        return [self.leftChild, self.rightChild]

    # This was called children during lecture. It's purpose is only
    # to visualize the tree. The above children method should replace it.
    def toList(self, *obj):
        node = self if len(obj) == 0 else obj[0]
        output = [node.key]
        left = node.getLeftChild()
        right = node.getRightChild()
        output.append(None if left == None else self.toList(left))
        output.append(None if right == None else self.toList(right))
        return output

    def __str__(self):
        return str(self.toList())

    # Adapted from: https://stackoverflow.com/questions/15214852/calculating-depth-of-a-binary-tree-in-python
    def height(self):
        left_height = self.getLeftChild().height() if self.getLeftChild() != None else -1
        right_height = self.getRightChild().height() if self.getRightChild() != None else -1
        return (left_height if left_height > right_height else right_height) + 1

class BinaryHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heaplist.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                self.heaplist[i // 2], self.heaplist[i] = self.heaplist[i], self.heaplist[i // 2]
            i = i // 2

    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        output = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.percDown(1)
        return output

    def build(self, valuelist):
        i = len(valuelist) // 2
        self.currentSize = len(valuelist)
        self.heaplist = [0] + valuelist[:]
        while i > 0:
            self.percDown(i)
            i -= 1

class BinarySearchTree:
    def __init__(self):
        self.tree = BinaryTree(None)

    def insert(self, key):
        node = self.tree
        while node.getRootVal() != None:
            if key < node.getRootVal():
                if node.getLeftChild() == None:
                    break
                node = node.getLeftChild()
            else:
                if node.getRightChild() == None:
                    break
                node = node.getRightChild()
        if node.getRootVal() == None:
            node.setRootVal(key)
        elif key < node.getRootVal():
            node.insertLeft(key)
        else:
            node.insertRight(key)

    #implement subscriptable [] class
    def __getitem__(self, key):
        node = self.tree
        while node.getRootVal() != None:
            if key < node.getRootVal():
                if node.getLeftChild() == None:
                    break
                node = node.getLeftChild()
            elif key > node.getRootVal():
                if node.getRightChild() == None:
                    break
                node = node.getRightChild()
            else:
                break
        return node if node.getRootVal() == key else None

    # contains can take advantage of the existing __getitem__ method.
    def contains(self, key):
        return self[key] != None

    # implement 'in' operator - uses contains method.
    def __contains__(self, key):
        return self.contains(key)

    # build can take advantage of the existing insert method.
    def build(self, list):
        for key in list:
            self.insert(key)
    
    # height overrides the BinaryTree height method.
    def height(self):
        return self.tree.height();

    # str overrides the BinaryTree __str__ method.
    def __str__(self):
        return self.tree.__str__()

    def delete(self, key):
        node = self[key]
        nodeIsLeftChild = node == node.parent.leftChild
        if node != None:
            # Leaf node - simply remove the node
            if node.leftChild == None and node.rightChild == None:
                if nodeIsLeftChild:
                    node.parent.leftChild = None
                else:
                    node.parent.rightChild = None
            # Node has only a left child - promote to parent's position.
            elif node.leftChild != None and node.rightChild == None:
                if nodeIsLeftChild:
                    node.parent.leftChild = node.leftChild
                else:
                    node.parent.rightChild = node.leftChild
                node.leftChild.parent = node.parent
            # Node has only a right child - promote to parent's position
            elif node.rightChild != None and node.leftChild == None:
                if nodeIsLeftChild:
                    node.parent.leftChild = node.rightChild
                else:
                    node.parent.rightChild = node.rightChild
                node.rightChild.parent = node.parent
            # Node has both left and right children - replace with sucessor.
            else:
                successor = node.leftChild
                while successor.rightChild != None:
                    successor = successor.rightChild

                # if successor is a leaf node...
                if successor.leftChild == None and successor.rightChild == None:
                    node.setRootVal(successor.getRootVal())
                    if successor.parent.leftChild == successor:
                        successor.parent.leftChild = None
                    else:
                        successor.parent.rightChild = None
                else:
                    successor.parent = node.parent
                    if nodeIsLeftChild:
                        node.parent.leftChild = successor
                    else:
                        node.parent.rightChild = successor
                    if successor != node.leftChild:
                        successor.leftChild = node.leftChild
                    if successor != node.rightChild:
                        successor.rightChild = node.rightChild

class Vertex:
    def __init__(self, key, value = None): # added value parameter
        self.id = key
        self.neighbors = []
        self.predecessors = [] # only pertains to directed graphs
        self.value = value

    def addNeighbor(self, vertex, directed = False):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
        if directed:  # Add self as predecessor to its neighbor
            self.neighbors[len(self.neighbors) - 1].predecessors.append(self)
        else: 
            if self not in vertex.neighbors:
                vertex.addNeighbor(self)

class Graph:
    def __init__(self, directed = False):
        self.vertices = {}
        self.directed = directed
        self.edgedict = {}
        
    def size(self):
        return len(self.vertices)

    def __getitem__(self, key):
        return self.vertices[key]

    def __contains__(self, key):
        return key in self.vertices

    # Updated this to allow adding a Vertex object or a key value.
    def addVertex(self, *v):
        for key in v:
            if type(key) is Vertex:
                self.vertices[key.id] = Vertex(key.id, key.value)
            else:
                if key not in self:
                    self.vertices[key] = Vertex(key)

    def edges(self):
        output = []
        for key in self.vertices.keys():
            for vertex in self.vertices[key].neighbors:
                kvp = (key, vertex.id)
                if kvp not in output: 
                    output.append(kvp)
        return output

    def __iter__(self):
        return iter(self.vertices.values())

    
    def addEdge(self, start, weight = 0, *end):
        for key in end:
            if key in self:
                self[start].addNeighbor(self[key], self.directed)
                kvp = (start, key)
                if kvp in self.edges():
                    self.edgedict[kvp] = weight

    def edge(self, start, end):
        if type(start) == Vertex:
            start = start.id
        if type(end) == Vertex:
            end = end.id
        kvp = (start, end)
        rvp = (end, start)
        if kvp in self.edgedict:
            return self.edgedict[kvp]
        if not self.directed and rvp in self.edgedict:
            return self.edgedict[rvp]
        return None