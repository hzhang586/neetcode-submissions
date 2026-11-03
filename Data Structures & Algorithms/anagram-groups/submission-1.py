class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        words = defaultdict(list)

        for s in strs:
            char_count = [0]*26
            for c in s:
                char_count[ord(c)-ord('a')] += 1
            
            words[tuple(char_count)].append(s)
        

        ans = []
        for key in words:
            ans.append(words[key])
        
        return ans


        