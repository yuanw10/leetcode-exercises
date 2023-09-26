# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_cur = l1
        l2_cur = l2
        result = ListNode(None, None)
        res_cur = result
        carry = 0

        while l1_cur or l2_cur or carry:

            if l1_cur and l2_cur:
                add = l1_cur.val + l2_cur.val + carry
                l1_cur = l1_cur.next
                l2_cur = l2_cur.next
            elif l1_cur:
                add = l1_cur.val + carry
                l1_cur = l1_cur.next
            elif l2_cur:
                add = l2_cur.val + carry
                l2_cur = l2_cur.next
            else:
                add = carry

            if add >= 10:
                carry = 1
                add -= 10
            else:
                carry = 0

            res_cur.next = ListNode(add, None)
            res_cur = res_cur.next
            
        return result.next
            