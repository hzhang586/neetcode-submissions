class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        ans = []
        for i in range(len(nums)):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            
            if i - dq[0] >= k:
                dq.popleft()
            
          
            if i >= k-1:
                ans.append(nums[dq[0]])
        
        return ans



        