'''
############## Construct binary Tree from Inorder and Postorder ###############
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


leetcode : https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

'''

# solution
# approach 1 : recursive
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.index = len(postorder)
        self.d = {}

        def construct(i, j):
            if i >= j:
                return None

            self.index -= 1

            temp = TreeNode(postorder[self.index])

            k = self.d.get(postorder[self.index], i)
            while k < j:
                if inorder[k] == postorder[self.index]:
                    self.d[inorder[k]] = k
                    break

                self.d[inorder[k]] = k
                k += 1

            temp.right = construct(k+1, j)
            temp.left = construct(i, k)

            return temp

        return construct(0, len(postorder))