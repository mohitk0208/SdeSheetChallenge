'''
###################### Serialize and deserialize BT #################
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



leetcode : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

'''


# solution
# approach 1 : using preorder traversal
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        pre = []
        def preorder(node):
            if node == None:
                pre.append("N")
                return

            pre.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return ",".join(pre)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        pre = data.split(",")
        self.i = -1
        def construct(pre):
            self.i += 1
            if pre[self.i] == "N":
                return None

            temp = TreeNode(int(pre[self.i]))
            temp.left = construct(pre)
            temp.right = construct(pre)

            return temp

        return construct(pre)