# Miguel de la Cruz Cabello
# Professor Merritt
# COMS 326
# 5 April 2021

import operator
# The BinaryTree class is provided here because the ParseTree class (below)
# uses it. Do not modify the BinaryTree class.
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
    def children(self):
        return [self.leftChild, self.rightChild]
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
# DO NOT CHANGE ANY CODE ABOVE THIS LINE --------------------------------

# Extend/modify this class to complete this assignment. See instructions on MyBLC.
class ParseTree():
    def getTokens(self):
        l = [""] # List of tonkens
        for i in list(self.expression):
            if i.isdigit() and l[-1].isdigit(): #Checks if the elemnts are digits
                l[-1] += i # Last character is equal to the last character + i
            else:
                l.append(i)# Adds the item to the list
        return l[1:] # Rteruns elemnt 1 to the last element of the list

        # Other way
##        output = []
##        tokens = list(self.expression)
##        i = 0 # Counter
##        while i in range(len(tokens)):
##            token = tokens[i]
##            if token in "()+-/*":
##                output.append(token)          
##            else:
##                while i < len(tokens) - 1 and tokens[i + 1].isnumeric():
##                    token = token + tokens[i + 1]
##                    i += 1
##                output.append(token)
##            i += 1
##        return output
    
    def __init__(self, expression):
        self.expression = expression
        self.tree = BinaryTree(None)
        tokens = self.getTokens()
        currentNode = self.tree
        for token in tokens:
            if token == '(':
                if currentNode.leftChild == None:
                    currentNode = currentNode.insertLeft(None)
                else:
                    currentNode = currentNode.leftChild
            elif token.isnumeric():              
                currentNode.setRootVal(int(token))
                currentNode = currentNode.parent
            elif token in "+-*/":                   
                currentNode.setRootVal(token)
                if currentNode.rightChild == None:
                    currentNode = currentNode.insertRight(None);
                else:
                    currentNode = currentNode.rightChild
            elif token == ')':                      
                currentNode = currentNode.parent
            else:
                raise ValueError("Unknown Operator: " + token)

    def __str__(self):
        return str(self.tree)

    def evaluate(self, *obj):
        opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        t = self.tree if len(obj) == 0 else obj[0]
        left = t.getLeftChild()
        right = t.getRightChild()
        if left and right:              
            fn = opers[t.getRootVal()]
            return fn(self.evaluate(left), self.evaluate(right))         
        else:
            return t.getRootVal()


# Example implementation of ParseTree class...
exp = "(21+(10*5))"
p = ParseTree(exp)
print(p)
result = p.evaluate()
print(result)



