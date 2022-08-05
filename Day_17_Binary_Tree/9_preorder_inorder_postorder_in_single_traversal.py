'''
########################## Tree Traversals ######################
You have been given a Binary Tree of 'N' nodes, where the nodes have integer values. Your task is to find the ln-Order, Pre-Order, and Post-Order traversals of the given binary tree.

codestudio : https://www.codingninjas.com/codestudio/problems/981269?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

'''

# solution
# approach 1 : recursive
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    ino = []
    pre = []
    post = []

    def traversal(r):
        if r == None:
            return

        pre.append(r.data)
        traversal(r.left)
        ino.append(r.data)
        traversal(r.right)
        post.append(r.data)

    traversal(root)

    return [ino, pre, post]