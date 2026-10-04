class Solution:

    def create_map(self,s:str) -> tuple:
        s_map = [0]*26
        for c in s:
            s_map[ord(c)-ord('a')] += 1
        return tuple(s_map)
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = self.create_map(s)
        t_map = self.create_map(t)
        return s_map == t_map