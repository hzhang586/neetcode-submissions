class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        canBreak = [False]*(n+1)
        canBreak[0] = True

        wordDict_set = set(wordDict)

        word_len = [len(word) for word in wordDict]
        max_len,min_len = max(word_len),min(word_len)

        for i in range(1,n+1):
            for j in range(min_len,max_len+1):
                if i-j >= 0 and canBreak[i-j] and s[i-j:i] in wordDict_set:
                    canBreak[i] = True
                    break
        
        return canBreak[-1]
        