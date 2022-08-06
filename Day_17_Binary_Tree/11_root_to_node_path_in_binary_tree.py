'''
################## Node to root path in binary tree ###############
Given a Binary Tree A containing N nodes.

You need to find the path from Root to a given node B.

NOTE:

No two nodes in the tree have same data values.
You can assume that B is present in the tree A and a path always exists.


interviewbit : https://www.interviewbit.com/problems/path-to-given-node/

'''


# solution
# approach 1 : simple preorder traversal
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        ans = []
        def traversal(node):
            if node == None:
                return False

            if node.val == B:
                ans.append(node.val)
                return True

            if traversal(node.left) or traversal(node.right):
                ans.append(node.val)
                return True

            return False

        traversal(A)

        ans.reverse()
        return ans