'''
################### BST Iterator #################
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.


leetcode : https://leetcode.com/problems/binary-search-tree-iterator/

'''


# solution
# this basically mimics the iterative inorder traversal
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root != None:             # go the leftest node and store all nodes in path
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        x = self.stack.pop()        # pop the last element

        y = x.right
        while y != None:            # if x has right node then go to leftest node and store all node in the path to the stack
            self.stack.append(y)
            y = y.left

        return x.val

    def hasNext(self) -> bool:      # if the stack becomes empty the traversal of the BT is complete
        return len(self.stack) != 0