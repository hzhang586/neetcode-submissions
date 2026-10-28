class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        ans = ""

        def expand(left,right):
            nonlocal ans

            while left >= 0 and right < n and s[left] == s[right]:

                if right - left + 1 > len(ans):
                    ans = s[left: right+1]
                
                left -= 1
                right += 1
            
        for i in range(n):
                expand(i,i)
                expand(i,i+1)
            
        return ans
        