class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        ans = 0
        i = 0
        j = 0
        n = len(s)
        c_dict = defaultdict(int)
        maxFreq = 0

        while j < n:
            c_dict[s[j]] += 1
            maxFreq = max(c_dict[s[j]],maxFreq)
            while j-i+1 - maxFreq > k:
                c_dict[s[i]] -= 1
                i += 1
            
            ans = max(j-i+1,ans)
            j += 1
        
        return ans




        