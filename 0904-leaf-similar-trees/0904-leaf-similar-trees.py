# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        stack1, stack2 = [root1], [root2]
        seq1, seq2 = [],[]
        while stack1:
            cur=stack1.pop()
            if cur.right:
                stack1.append(cur.right)
            if cur.left:
                stack1.append(cur.left)
            if not cur.right and not cur.left:
                seq1.append(cur.val)
        while stack2:
            cur=stack2.pop()
            if cur.right:
                stack2.append(cur.right)
            if cur.left:
                stack2.append(cur.left)
            if not cur.right and not cur.left:
                seq2.append(cur.val)
        return seq1==seq2
