# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        trav = []
        self.postorder(root, trav)
        return trav

    def postorder(self, root, trav):
        if root:
            self.postorder(root.left, trav)
            self.postorder(root.right, trav)
            trav.append(root.val)
        