'''
######################## Vertical Order Traversal of a Binary Tree ##############
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

leetcode : https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

'''

# solution
# approach 1: recursive
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}

        # here the row denotes the level and col denotes the hoe=rizontal distance

        def traversal(node, hd, level ):
            if node == None:
                return

            traversal(node.left, hd-1, level+1)
            traversal(node.right, hd+1, level+1)

            d[hd] = d.get(hd, [])
            d[hd].append((level, node.val))


        traversal(root, 0, 0)
        ans = []
        for k, v in sorted(d.items()):
            ans.append(list(map(lambda x:x[1], sorted(v) )))

        return ans