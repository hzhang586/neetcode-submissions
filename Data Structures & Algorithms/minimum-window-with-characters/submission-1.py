class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n1 = len(s)
        n2 = len(t)
        if n2 > n1:
            return ""
        min_len = float("inf")
        ans = ""
        i = 0
        j = 0
        need = Counter(t)
        required = len(need)
        have = 0
        window = Counter()
        
        for j in range(len(s)):
            c = s[j]
            window[s[j]] += 1

            if c in need and need[c] == window[c]:
                have += 1
            
            while have == required:
                if j-i+1 < min_len:
                    min_len = j-i+1
                    ans = s[i:j+1]
                
                left_char = s[i]
                if left_char in need and need[left_char] == window[left_char]:
                    have -= 1
                
                window[left_char] -= 1
                i += 1

        
        return ans


            

        