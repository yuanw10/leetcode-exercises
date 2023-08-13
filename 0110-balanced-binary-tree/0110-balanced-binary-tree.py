# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            cur = queue.pop()
            if cur:
                le_dep = self.getDepth(cur.left)
                ri_dep = self.getDepth(cur.right)
                if abs(le_dep - ri_dep) > 1:
                    return False
                cur.left and queue.append(cur.left)
                cur.right and queue.append(cur.right)
        return True

    def getDepth(self, root):
        if root:
            return 1 + max(self.getDepth(root.left), self.getDepth(root.right))
        else:
            return 0

