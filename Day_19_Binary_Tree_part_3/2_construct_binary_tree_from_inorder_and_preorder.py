'''
##################### Construct Binary Tree from Inorder and Preorder ##############
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


leetcode : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

'''


# solution
# approach 1 : recursive
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index = -1
        self.d = {}

        def construct(i, j ):
            if i >= j:
                return None

            self.index += 1

            temp = TreeNode(preorder[self.index])

            split_point = i
            for k in range(i, j):
                if inorder[k] == preorder[self.index]:
                    split_point = k
                    break

            temp.left = construct(i, k)
            temp.right = construct(k+1, j)

            return temp

        return construct(0, len(preorder))