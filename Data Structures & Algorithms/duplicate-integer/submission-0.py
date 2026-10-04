class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        unique = set(nums)
        return len(nums) > len(unique)
        