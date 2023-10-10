# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        in_trav = []
        self.inorder(root, in_trav)
        return in_trav
    
    def inorder(self, root, trav):
        if root:
            self.inorder(root.left, trav)
            trav.append(root.val)
            self.inorder(root.right, trav)
        else:
            return