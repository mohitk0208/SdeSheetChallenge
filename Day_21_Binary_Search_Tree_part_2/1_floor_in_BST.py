'''
################## Floor in BST ################
You are given a BST (Binary search tree) with’ N’ number of nodes and a value ‘X’. Your task is to find the greatest value node of the BST  which is smaller than or equal to  ‘X’.

codestudio : https://www.codingninjas.com/codestudio/problems/floor-from-bst_920457?source=youtube&campaign=Striver_Tree_Videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=Striver_Tree_Videos&leftPanelTab=0


'''


# solution
# approach 1 : inorder traversal
# find the inorder traversal and stop when a node with greater value than X is found
# the last node of inorder traversal is the answer
def floorInBST(root, X):

    ino = []
    found = [False]

    def inorder(node):
        if node == None or found[0]:
            return

        inorder(node.left)
        if node.data > X:
            found[0] = True
            return

        ino.append(node.data)
        inorder(node.right)

    inorder(root)

    return ino[-1]




# approach 2: recursive
def floorInBST(root, X):
    if root == None:
        return None

    if root.data > X:
        return floorInBST(root.left, X)

    if root.data == X:
        return root.data

    ans = None
    if root.right != None:
        ans = floorInBST(root.right, X)

    return root.data if ans == None else ans
