class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []

        nums = sorted(nums)

        for i,x in enumerate(nums):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -x
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] == target:
                    ans.append([x,nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j< k and nums[k] == nums[k+1]:
                        k -= 1

                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        
        return ans
            



        
        