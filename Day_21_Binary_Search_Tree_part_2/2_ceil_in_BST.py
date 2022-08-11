'''
#################### Ceil in BST ####################
Ninja is given a binary search tree and an integer. Now he is given a particular key in the tree and returns its ceil value. Can you help Ninja solve the problem?


codestudio : https://www.codingninjas.com/codestudio/problems/ceil-from-bst_920464?source=youtube&campaign=Striver_Tree_Videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=Striver_Tree_Videos&leftPanelTab=0

'''


# solution
# approach 1 : loop
def findCeil(root, x):

    ceil = -1                     # initialize ceil
    while root:
        if root.data == x:        # ceil is x
            return x

        if root.data > x:         # ceil maybe current node or in the left
            ceil = root.data
            root = root.left
        else:
            root = root.right    # ceil is in the right or does not exist

    return ceil