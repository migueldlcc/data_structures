class Node:
    def __init__(self, *initdata):
        self.next = None
        if len(initdata) > 0:
            self.data = initdata[0]
        else:
            self.data = None
    def setData(self, newdata):
       self.data = newdata

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
        sel.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
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
        while self.head.getdata() == value:
            self.head = self.head.getNext()
        current = self.head
        while current != None:
            next = current.getNext()
            if next.getData() == value:
                current.setNext(nect.getNext())
            current = current.getNext()

    def __len__(self):
        return self.length()

    def __iadd__(self, item):
        self.add(item)
        return 

    def __contains__(self,value):
        return self.search(value)

    #list 3.4 on the book, use it for almost all assignment 3

class OrderedList:
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
                    corNode = corNode.getNext()
            newNode.setNext(curNode)
            prevNode.setNext(newNode)

    def search(self, value):
        current = self.head
        while current != None:
            if current.getData() == value:
                return True
            if current.getData() > value:
                return False
            current = current.getNext()
        return False

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
