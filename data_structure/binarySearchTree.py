#
# Binary Search Tree
# author: Valentin Lehuger
#
# Insertion complexity:
#       average: O(log(n))
#       worst: O(n)
#
# Space complexity: O(n)


# To do

# One class TreeNode
#         __init__
#         hasLeftChild
#         hasRightChild
#         isLeftChild
#         isRightChild
#         isRoot
#         isLeaf
#         hasAnyChildren
#         hasBothChildren
#         replaceNodeData
        

# One class BinarySearchTree
#         __init__
#         length
#         __len__
#         put
#         _put
#         __setitem__
#         get
#         _get
#         __getitem__
#         __contains__
#         delete
#         __delitem__
#         spliceOut
#         findSuccessor
#         findMin
#         findMax
#         mean
#         median
#         remove





class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = None
        self.leftChild = None
        self.rightChild = None


    def isRoot(self):
        """ Return: boolean """
        return not self.parent

    def isLeaf(self):
        """ Return: boolean """
        return not (self.leftChild or self.rightChild)


    def insert(self, value):
        """ 
        Insert the value sorted. In the worst case,
        the complexity is O(n) if the root node is the values
        to insert are always sorted.
        """
        if value < self.value:
            if self.leftChild == None:
                self.leftChild = Node(value, self)
            else:
                self.leftChild.insert(value)
        else:
            if self.rightChild is None:
                self.rightChild = Node(value, self)
            else:
                self.rightChild.insert(value)

    def delete(self, value):
        if value == self.value
        if value < self.value:

    def getMin(self):
        if self.rightChild:
            return self.rightChild.getMin()
        return self.value

    def printTree(self):
        """ Print the entire tree from left to right."""
        if self.leftChild:
            # print "Go left"
            self.leftChild.printTree()
            # print "UP"
        print self.value
        if self.rightChild:
            # print "Go right"
            self.rightChild.printTree()
            # print "UP"



if __name__ == "__main__":

    bst = Node(5)

    for el in [2, 19, 4, 18, 7, 1, 6, 3, 13]:
       bst.insert(el)

    bst.printTree()
