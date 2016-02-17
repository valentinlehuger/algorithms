
class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, value):
        tmp = Node(value)
        tmp.leftChild = self.leftChild
        self.leftChild = tmp

    def insertRight(self, value):
        tmp = Node(value)
        tmp.rightChild = self.rightChild
        self.rightChild = tmp

    def getLeft(self):
        return self.leftChild

    def getRight(self):
        return self.rightChild

    def getValue(self):
        return self.value

    def printTree(self):
        if self.leftChild is not None:
            self.leftChild.printTree()
        print self.value
        if self.rightChild is not None:
            self.rightChild.printTree()


if __name__ == "__main__":

    root = Node('a')
    root.insertLeft('b')
    root.insertRight('c')
    root.getLeft().insertRight('d')
    root.getRight().insertLeft('e')
    root.getRight().insertRight('f')
    root.printTree()
