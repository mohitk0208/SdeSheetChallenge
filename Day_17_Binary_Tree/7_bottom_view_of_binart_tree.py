'''
###################### Bottom View of Binary Tree ################
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.
If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \
                 10       14

For the above tree the output should be 5 10 4 14 25.


gfg : https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

'''


# solution
# approach 1: recursive (reverse postOrder traversal)
class Solution:
    def bottomView(self, root):
        d = {}                      # it stores the [horizontal distance] : (node data, level)

        def reversePostorder(node, hd, level):
            if node == None:
                return

            reversePostorder(node.right, hd+1, level+1)
            reversePostorder(node.left, hd-1, level+1)


            # store the rightmost and the bottommost node for every horizontal distance
            if hd in d:
                if d[hd][1] < level:
                    d[hd] = (node.data, level)
            else:
                d[hd] = (node.data, level)


        reversePostorder(root, 0, 0)
        ans = map(lambda x:x[1][0], sorted(d.items())) # get the node sorted according to horizontal distance

        return ans


