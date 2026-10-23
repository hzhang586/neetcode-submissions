class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        start = self.binarySearch(nums,target)
        if start == n or nums[start] != target:
            return [-1,-1]
        
        end = self.binarySearch(nums,target+1)-1

        return [start,end]
        






    def binarySearch(self,nums: List[int], target: int) -> int:

        n = len(nums)
        left, right = -1,n

        while left+1 < right:
            mid = (left+right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        return right
        