'''
##################### Kth smallest element in BST ################
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


leetcode : https://leetcode.com/problems/kth-smallest-element-in-a-bst/

'''

# solution
# approach 1 : inorder traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.num = 0
        self.ans = -1

        def inorder(node):
            if node == None or self.ans != -1:
                return


            inorder(node.left)
            self.num +=1
            if self.num == k:
                self.ans = node.val
                return
            inorder(node.right)

        inorder(root)

        return self.ans