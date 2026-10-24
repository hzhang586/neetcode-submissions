# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        head1 = head
        head2 = slow.next
        slow.next = None

        prev = None
        cur = head2

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        head2 = prev

        cur1 = head1
        cur2 = head2


        

        cur3 = cur1
        cur1 = cur1.next
        counter = 1
        while cur1 and cur2:
            print(counter)
            if counter % 2:  
                cur3.next = cur2
                cur2 = cur2.next
            else:
                cur3.next = cur1
                cur1 = cur1.next
            cur3 = cur3.next
            counter += 1


        
        cur3.next = cur1

        