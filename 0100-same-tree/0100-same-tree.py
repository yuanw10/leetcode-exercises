# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
    #     trav_lnr1=[]
    #     trav_lnr2=[]
    #     trav_nlr1=[]
    #     trav_nlr2=[]

    #     self.lnr(p, trav_lnr1)
    #     self.lnr(q, trav_lnr2)
    #     self.nlr(p, trav_nlr1)
    #     self.nlr(q, trav_nlr2)

    #     return trav_lnr1==trav_lnr2 and trav_nlr1==trav_nlr2
        
    # def lnr(self, root, arr):
    #     if not root:
    #         arr.append(-1)
    #         return
    #     self.lnr(root.left, arr)
    #     arr.append(root.val)
    #     self.lnr(root.right, arr)
    
    # def nlr(self, root, arr):
    #     if not root:
    #         arr.append(-1)
    #         return
    #     arr.append(root.val)
    #     self.nlr(root.left, arr)
    #     self.nlr(root.right, arr)

        if p and q and p.val==q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False