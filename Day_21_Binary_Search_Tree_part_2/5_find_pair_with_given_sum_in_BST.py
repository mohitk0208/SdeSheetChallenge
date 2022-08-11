'''
################## Find pair with given sum in BST #############
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.


leetcode : https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

'''


# solution
# approach 1: recursive check
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.d = set([])

        def check(node):
            if node == None:
                return False

            t = k - node.val

            if t in self.d:
                return True

            self.d.add(node.val)

            n = node.left if t < node.val else node.right

            while n != None:

                if n.val == t:
                    return True

                if n.val > k:
                    n = n.left
                else:
                    n = n.right

            return check(node.left) or check(node.right)


        return check(root)



# approach 2 : inorder traversal
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        ino = []

        def inorder(node):
            if node == None:
                return

            inorder(node.left)
            ino.append(node.val)
            inorder(node.right)

        inorder(root)

        i = 0
        j = len(ino) - 1
        sum_ = ino[0] + ino[j]

        while i < j:
            sum_ = ino[i] + ino[j]
            if sum_ == k:
                return True

            if sum_ < k:
                i += 1
            else:
                j -= 1

        return False