# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur=head
        pre=None
        while cur != None:
            temp = cur.next
            cur.next= pre
            pre = cur
            cur = temp
        return pre
