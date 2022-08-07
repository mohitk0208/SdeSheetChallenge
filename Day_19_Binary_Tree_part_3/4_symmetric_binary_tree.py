'''
################# Symmetric Binary tree ######################
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


leetcode : https://leetcode.com/problems/symmetric-tree/

'''


# solution
# approach 1 : recursive
class Solution:

    def _isSymmetric(self, first, second):
        if first == None and second == None:
            return True


        if first != None and second != None and self._isSymmetric(first.left, second.right) and self._isSymmetric(first.right, second.left):

            return first.val == second.val

        return False


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            if root == None:
                return True

            return self._isSymmetric(root.left, root.right)