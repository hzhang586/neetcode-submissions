# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        cur1 = l1
        cur2 = l2
        flag = 0

        dummy = ListNode()
        cur3 = dummy

        while cur1 and cur2:
            digit_sum = cur1.val + cur2.val+ flag
            flag = 1 if digit_sum >= 10 else 0
            cur3.next = ListNode(digit_sum%10)
            cur3 = cur3.next

            cur1 = cur1.next
            cur2 = cur2.next

        cur = cur1 if not cur2 else cur2

        while cur:
            digit_sum = cur.val + flag
            flag = 1 if digit_sum >= 10 else 0
            cur3.next = ListNode(digit_sum%10)
            cur = cur.next
            cur3 = cur3.next
        
        if flag:
            cur3.next = ListNode(1)
            cur3 = cur3.next
        
        return dummy.next

