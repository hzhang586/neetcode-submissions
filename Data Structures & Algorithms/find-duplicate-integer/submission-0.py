class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        fast = slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                cur = 0
                while cur != slow:
                    cur = nums[cur]
                    slow= nums[slow]
                
                return cur
                