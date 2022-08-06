'''
####################  Binary Tree Level Order Traversal ################
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


leetcode : https://leetcode.com/problems/binary-tree-level-order-traversal/

'''


# solution
# approach 1: recursive
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        d = {}

        def preorder(node, level):
            if node == None:
                return

            try:
                d[level].append(node.val)
            except KeyError:
                d[level] = [node.val]


            preorder(node.left, level+1)
            preorder(node.right, level+1)


        preorder(root, 0)

        ans = list(map(lambda x:x[1], sorted(d.items())))

        return ans



# approach 2: iterative
from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []


        q = Queue()

        q.put(root)

        ans = []

        while len(q.queue) != 0:

            x = []
            y = Queue()
            while len(q.queue) != 0:
                node = q.get()
                x.append(node.val)

                if node.left != None :
                    y.put(node.left)

                if node.right != None:
                    y.put(node.right)

            ans.append(x)
            q = y


        return ans
