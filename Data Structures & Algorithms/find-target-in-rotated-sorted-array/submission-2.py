class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left, right = -1,n

        while left+1 < right:

            mid = (left+right) // 2

            if nums[mid] == target:
                return mid

            if nums[left+1] <= nums[mid]:
                if nums[left+1] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            
            else:
                if nums[mid] < target <= nums[right-1]:
                    left = mid
                else:
                    right = mid
        
        return -1
