'''
##################### Zig Zag Traversal of binary Tree ##############
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).


leetcode : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

'''

# solution
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}

        def traversal(node, level):
            if node == None:
                return

            traversal(node.left, level+1)
            try:
                d[level].append( node.val)
            except KeyError:
                d[level] = [node.val]

            traversal(node.right, level+1)

        traversal(root, 0)

        ans = []
        isReverse = False
        for k, v in sorted(d.items()):
            ans.append(v)
            if isReverse:
                ans[-1].reverse()
            isReverse = not isReverse

        return ans