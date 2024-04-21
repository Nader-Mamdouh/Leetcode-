# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        
        prev, cur = head, head.next
        
        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue

            tmp = dummy
            while tmp.next.val < cur.val:
                tmp = tmp.next
            
            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next
        
        return dummy.next
