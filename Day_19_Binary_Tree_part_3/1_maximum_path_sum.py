'''
#################### Maximum path sum ####################
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


leetcode : https://leetcode.com/problems/binary-tree-maximum-path-sum/

'''

# solution
# approach 1 : recursive
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.ans = float("-inf")          # initial answer

        def dp(node):

            if node == None:              # if the node is null, it does not contribute to ans
                return 0


            l = dp(node.left)             # maximum value obtained from left node
            r = dp(node.right)            # maximum value obtained from right node

            temp1 = node.val + l + r      # if node is the root of the path that has maximum sum
            temp2 = node.val + max(l, r)  # if maximum path passes through the node
                                          # node.val if maximum path starts from the node
            self.ans = max(self.ans, temp1, temp2, node.val)   # choose which is maximum

            return max(temp2, node.val)


        t = dp(root)
        self.ans = max(self.ans, t)

        return self.ans