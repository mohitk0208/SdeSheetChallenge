'''
################# Populate next right pointer of Tree ###########
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


leetcode : https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

'''

# solution
# approach 1 : level order traversal OR BFS
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if root == None:
            return None

        q = Queue()
        q.put(root)

        while len(q.queue) != 0:
            y = Queue()

            x = q.get()
            if x.left != None:
                y.put(x.left)

            if x.right != None:
                y.put(x.right)

            while len(q.queue) != 0:

                z = q.get()
                x.next = z
                x = z
                if z.left != None:
                    y.put(z.left)

                if z.right != None:
                    y.put(z.right)

            q = y

        return root