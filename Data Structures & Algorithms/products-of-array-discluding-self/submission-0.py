class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zero_count = 0
        ans = [0]*len(nums)
        product = 1
        for i,x in enumerate(nums):
            if x == 0:
                zero_count += 1
                if zero_count > 1:
                    return [0]*len(nums)
            else:
                product *= x
        print(product)
        if zero_count == 0:
            for i,x in enumerate(nums):
                ans[i] = int(product/x)
        else:
            for i,x in enumerate(nums):
                if x == 0:
                    ans[i] = product

       
        return ans
        