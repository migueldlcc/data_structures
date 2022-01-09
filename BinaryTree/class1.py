import BinaryTree

class BinarySearchTree:
    def __init__(self):
        self.tree = BinaryTree.BinaryTree(None)

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

    def __str__(self):
        return self.tree.__str__()

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

    def contains(self, key):
        return self[key] != None

    def __contains__(self, key):
        return self[key] != None

    def height(self):
        return self.tree.height()

    def build(self, list):
        for key in list:
            self.insert(key)



bst = BinarySearchTree()
l = [2,1,8,4,5,3,21,98,65]
bst.build(l)
print(bst)
print(7 in bst)
print(4 in bst)
print(bst.height())




