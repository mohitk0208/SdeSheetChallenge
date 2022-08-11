'''
################ Kth Largest element in BST ##############
Given a Binary search tree. Your task is to complete the function which will return the Kth largest element without doing any modification in Binary Search Tree.


gfg : https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1

'''


# solution
# approach 1 : reverse inorder traversal
class Solution:
    def kthLargest(self,root, k):
        self.ans = -1
        self.num = 0

        def reverse_inorder(node):
            if node == None or self.ans != -1:
                return

            reverse_inorder(node.right)
            self.num += 1
            if self.num == k:
                self.ans = node.data
                return
            reverse_inorder(node.left)

        reverse_inorder(root)
        return self.ans