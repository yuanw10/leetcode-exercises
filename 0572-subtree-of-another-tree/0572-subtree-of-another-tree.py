# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        root_arr=[root]
        while root_arr:
            cur=root_arr.pop()
            if cur.val == subRoot.val and self.sameTree(cur, subRoot):
                return True
            cur.left and root_arr.append(cur.left)
            cur.right and root_arr.append(cur.right)
        return False

    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and root2 and root1.val == root2.val:
            return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
        else:
            return False
        