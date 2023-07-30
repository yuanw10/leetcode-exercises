# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal=[]
        self.preorder(root, traversal)
        return traversal

    def preorder(self, root, arr):
        if root:
            arr.append(root.val)
            self.preorder(root.left, arr)
            self.preorder(root.right, arr)
        else:
            return

