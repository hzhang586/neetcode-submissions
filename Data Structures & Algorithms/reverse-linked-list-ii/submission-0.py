# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        p0 = dummy
        for _ in range(left-1):
            p0 = p0.next
        
        prev = None
        cur = p0.next
        for _ in range(right-left+1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        p0.next.next = cur
        p0.next = prev

        return dummy.next