# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur=head
        while cur:
            if cur.val == -100001:
                return True
            cur.val=-100001
            cur=cur.next
        return False
