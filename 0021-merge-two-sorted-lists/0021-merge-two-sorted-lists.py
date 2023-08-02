# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head=None

        if list1 and list2 and list1.val<list2.val:
            head=list1
        elif list1 and list2 and list1.val>=list2.val:
            head=list2
        elif list1 and not list2:
            return list1
        else:
            return list2

        cur=head

        while list1 and list2:
            if list1.val < list2.val:
                temp=list1.next
                cur.next=list1
                list1=temp
            else:
                temp=list2.next
                cur.next=list2
                list2=temp
            cur=cur.next

        if list1 and not list2:
            cur.next=list1
        if list2 and not list1:
            cur.next=list2
            
        return head