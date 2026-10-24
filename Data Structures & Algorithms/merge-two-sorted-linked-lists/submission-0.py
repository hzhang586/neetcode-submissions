# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        
        if not list2:
            return list1
        
        cur1 = list1
        cur2 = list2
        head = None
        cur3 = None
        while cur1 and cur2:
            new_node = ListNode(cur1.val) if cur1.val <= cur2.val else ListNode(cur2.val)
            if cur1.val <= cur2.val:
                cur1 = cur1.next
            else:
                cur2 = cur2.next
            if not head:
                head = new_node
                cur3 = head
            else:
                cur3.next = new_node
                cur3 = cur3.next
        
        cur = cur1 if not cur2 else cur2

        while cur:
            cur3.next = ListNode(cur.val)
            cur = cur.next
            cur3 = cur3.next
        
        return head
        


