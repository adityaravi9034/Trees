from Trees.BinaryTree import Node
from LinearStructures import Queue


def preorder(root):
    if root:
        print(root.key)
        preorder(root.leftChild)
        preorder(root.rightChild)


def postorder(root):
    if root:
        postorder(root.leftChild)
        postorder(root.rightChild)
        print(root.key)


def inorder(root):
    if root:
        inorder(root.leftChild)
        print(root.key)
        inorder(root.rightChild)


def levelOrder(root):

    # Base Case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    q = Queue()

    # Enqueue Root and initialize height
    q.enqueue(root)

    while q.size() > 0:

        # Print front of queue and
        # remove it from queue
        currentNode = q.dequeue()
        print(currentNode.key)

        # Enqueue left child
        if currentNode.leftChild is not None:
            q.enqueue(currentNode.leftChild)

        # Enqueue right child
        if currentNode.rightChild is not None:
            q.enqueue(currentNode.rightChild)


if __name__ == "__main__":
    r = Node('Book')
    r.insertLeft('Chapter 1')
    r.leftChild.insertLeft('Section 1.1')
    r.leftChild.insertRight('Section 1.2')
    r.leftChild.rightChild.insertLeft('Section 1.2.1')
    r.leftChild.rightChild.insertRight('Section 1.2.2')
    r.insertRight('Chapter 2')
    r.rightChild.insertLeft('Section 2.1')
    r.rightChild.insertRight('Section 2.2')
    r.rightChild.rightChild.insertLeft('Section 2.2.1')
    r.rightChild.rightChild.insertRight('Section 2.2.2')

    print('PREORDER')
    preorder(r)
    print('\nINORDER')
    inorder(r)
    print('\nPOSTORDER')
    postorder(r)
    print('\nLEVEL ORDER')
    levelOrder(r)
