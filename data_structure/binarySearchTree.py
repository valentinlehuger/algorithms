
class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    
    def insertLeft(self, value):
        return

    def insertRight(self, value):
        return

    def insert(self, value):
        if value < self.value:
            if self.leftChild == None:
                self.leftChild = Node(value)
            else:
                self.lefChild.insert(value)
        else:
            if self.rightChild is None:
                self.rightChild = Node(value)
            else:
                self.rightChild.insert(value)
