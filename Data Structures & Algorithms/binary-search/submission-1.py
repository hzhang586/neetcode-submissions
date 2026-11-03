class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left,right = -1, len(nums)
        while left+1 < right:

            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        
        return -1
        