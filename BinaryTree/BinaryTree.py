class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None
        self.parent = None

    def getRootVal(self):
        return self.key
        
    def setRootValue(self, obj):
        self.key = obj

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild == BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
        self.leftChild.parent = self
        return self.leftChild

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild == BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
        self.rightChild.parent = self
        return self.rightChild

    def children(self, obj):
        return[self.leftChild, self.rightChild]

    def toList(self, *obj):
        node = self if len(obj) == 0 else obj[0]
        output = [node, key]
        left =  node.getLeftChild()
        right = node.getRightChild()
        output.append(None if left == None else self.toList(left))
        output.append(None if right == None else self.toList(right))
        return output

    def __str__(self):
        return str(self.toList())

p = BinaryTree(3)
p.insertLeft(4)
p.insertRight(5)
l = t.toList()
print(l)