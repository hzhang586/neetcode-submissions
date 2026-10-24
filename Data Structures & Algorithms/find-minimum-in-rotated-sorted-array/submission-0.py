class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        left = -1
        right = n

        while left+1 < right:

            mid = (left+right) // 2
            if nums[mid] > nums[-1]:
                left = mid
            else:
                right = mid
        
        return nums[right]



        