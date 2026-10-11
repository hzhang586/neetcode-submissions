class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        window_len = len(s1)
      
        s1_count = Counter(s1)

        i = 0
        j = window_len-1

        s2_count = Counter(s2[i:j+1])

        while j < n2:
            if s2_count == s1_count:
                return True
            
            if j == n2 - 1:
                break
            
            s2_count[s2[i]] -= 1
            i += 1
            j += 1
            s2_count[s2[j]] += 1
            
        return False

        