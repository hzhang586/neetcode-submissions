class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        ans = []
        for i,x in enumerate(nums):
            
            if dq and i - dq[0][0] == k:
                dq.popleft()
            
            while dq and nums[i] >= dq[-1][1]:
                dq.pop()
            dq.append((i,x))
            if i >= k-1:
                ans.append(dq[0][1])
        
        return ans



        