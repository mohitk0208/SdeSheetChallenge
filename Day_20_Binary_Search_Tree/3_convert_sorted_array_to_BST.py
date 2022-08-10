'''
################### Convert Sorted Array to BST #################
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

leetcode : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

'''

# solution
# approach 1 : recursive (normal tree traversal)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def construct(i, j):
            if i >= j:
                return None


            k = (i+j) // 2

            temp = TreeNode(nums[k])
            temp.left = construct(i, k)
            temp.right = construct(k+1, j)

            return temp

        return construct(0, len(nums))