'''
############## Construct a BST from Preorder traversal ################
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.


leetcode : https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

'''

# solution

# approach 1: recursive
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:


        def construct(i, j):
            if i >= j :
                return None

            temp = TreeNode(preorder[i])

            k = i+1                     # split point from which the elements are greater
            while k < j:
                if preorder[k] > preorder[i]:
                    break

                k += 1

            temp.left = construct(i+1, k)   # so from i+1 -> k the elements are smaller so on left
            temp.right = construct(k, j)  # so from k -> j the elements are larger so on the right

            return temp

        return construct(0, len(preorder))