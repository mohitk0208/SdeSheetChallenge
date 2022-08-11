'''
############### Find the Inorder predecessor and Successor of given node ########
There is BST given with root node with key part as an integer only. You need to find the in-order successor and predecessor of a given key. If either predecessor or successor is not found, then return -1 .


codestudio : https://www.codingninjas.com/codestudio/problems/893049?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

'''

# solution
# approach : brute force
def predecessorSuccessor(root, key):
    ino = []

    def inorder(node):
        if node == None:
            return

        inorder(node.left)
        ino.append(node.data)
        inorder(node.right)

    inorder(root)

    pre = -1
    succ = -1

    for i in range(len(ino)):
        if ino[i] == key:
            pre = -1 if i == 0 else ino[i-1]
            succ = -1 if i == len(ino) -1 else ino[i+1]
            break

    return [pre, succ]
