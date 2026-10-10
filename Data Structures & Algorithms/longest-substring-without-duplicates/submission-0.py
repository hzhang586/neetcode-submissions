class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        i = 0
        j = 0
        seen = set()

        while j < n:
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])

            ans = max(ans,j-i+1)
            j += 1
        return ans
                
                
            


