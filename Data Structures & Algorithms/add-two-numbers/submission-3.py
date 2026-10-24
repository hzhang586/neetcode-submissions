# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        cur1 = l1
        cur2 = l2
        carry = 0

        dummy = ListNode()
        cur3 = dummy

        while cur1 or cur2 or carry:
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0
            total = v1 + v2 + carry
            carry = total //10
            digit = total % 10
            cur3.next = ListNode(digit)
            cur3 = cur3.next

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
    
        
        return dummy.next

