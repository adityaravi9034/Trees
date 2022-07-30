class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = Node(newNode)
        else:
            t = Node(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = Node(newNode)
        else:
            t = Node(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

        return self.key

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


if __name__ == "__main__":
    r = Node('a')
    print(r.key)
    print(r.leftChild)
    r.insertLeft('b')
    print(r.leftChild.key)
    r.insertRight('c')
    print(r.rightChild.key)
    r.rightChild.key = 'Hello'
    print(r.rightChild.key)
    r.insertRight('d')
    print(r.rightChild.key)
    print(r.rightChild.rightChild.key)
    r.inorder()


