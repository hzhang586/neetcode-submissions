class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # n = len(nums)
        # return n*(n+1)//2- sum(nums)

        n = len(nums)
        ans = 0
        for i in range(n):
            ans ^= i
            ans ^= nums[i]
        
        return ans^n
        