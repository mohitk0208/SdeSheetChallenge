'''
###################### Left view of Binary tree ##################
Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.


gfg : https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/
'''


# solution
# approach 1 : iterative (results in Time Limit exceeded)
def LeftView(root):

    d = {}

    q = Queue()

    q.put((root,0))

    while len(q.queue) != 0:
        x = q.get()

        if x[1] not in d:
            d[x[1]] = x[0].data

        if x[0].left != None:
            q.put((x[0].left, x[1] +1))

        if x[0].right != None:
            q.put((x[0].right, x[1] +1))



    return d.values()




# approach 2 : recursive (more optimized)

def LeftView(root):

    ds = []

    def preorder(node, level):
        if node == None:
            return

        if level == len(ds):
            ds.append(node.data)

        preorder(node.left, level+1)
        preorder(node.right, level+1)

    preorder(root, 0)

    return ds
