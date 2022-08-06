'''
################### Max width of Binary Tree ###################
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.


leetcode : https://leetcode.com/problems/maximum-width-of-binary-tree/

'''


# solution
# approach 1: traversal
# here i pass the position of a node from top-to-bottom and left-to-right in sequential order
# and store the min and max for each level
# then I get the difference from each level and return the maximum
class Solution:

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        d = {}                          # [level]: (minimum position, maximum position)

        def traversal(node, level, pos):
            if node == None:
                return

            if level in d:
                d[level] = (min(pos, d[level][0]), max(pos, d[level][1]))
            else:
                d[level] = (pos, pos)

            x = pos<<1          # use shift operator to multiply by 2
            traversal(node.left, level+1, x)        # left child is 2n
            traversal(node.right, level+1, x+1)     # right child is 2n+1

        traversal(root, 0, 1)

        ans = max(map(lambda x:x[1]-x[0]+1, d.values())) # get maximum difference for each level

        return ans
