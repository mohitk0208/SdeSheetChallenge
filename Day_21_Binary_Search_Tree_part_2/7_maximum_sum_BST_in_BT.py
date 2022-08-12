'''
################### Maximum sum BST in BT ##################
Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


leetcode : https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

'''


# solution
# approach 1 : recursive
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        # The function returns the (sum of all children, minimum value among them, maximum value)
        def maxBST(node):
            if node == None:        # if node is None then
              # sum of children = 0
              # minimum is set to inf and maximum to -inf to so the parent is always valid
                return (0, float("inf"), float("-inf"))

            # if node is leaf then it is a BST
            if node.left == None and node.right == None:
                self.ans = max(self.ans, node.val)

            l = maxBST(node.left)
            r = maxBST(node.right)

            sum_ = node.val + l[0] + r[0] #sum of node and its children
            # if largest of left < node.val < smallest of right then it is BST
            if l[2] < node.val < r[1]:
                self.ans = max(self.ans, sum_)
                return (sum_, min(node.val, l[1], r[1]), max(node.val, l[2], r[2]))

            # if node is not BST then all nodes above are also not BST
            # so set minimum to -inf and maximum to inf
            # so any parent node will never satisfy the condition
            return (sum_, float("-inf"), float("inf"))

        maxBST(root)

        return self.ans