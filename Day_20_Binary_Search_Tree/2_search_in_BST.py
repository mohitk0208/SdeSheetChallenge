'''
################# Search in BST ################
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null


leetcode : https://leetcode.com/problems/search-in-a-binary-search-tree/

'''

# solution
# approach 1 : loop
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root

        while temp is not None:
            if val == temp.val:
                return temp

            if val < temp.val:
                temp = temp.left
            else:
                temp = temp.right

        return None



# approach 2 : recursive
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None

        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)