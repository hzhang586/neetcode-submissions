class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        words = set(wordList)
        if endWord not in words or beginWord == endWord:
            return 0
        
        n = len(endWord)
        visited = set()
        visited.add(endWord)
        queue = deque([(1,endWord)])

        while queue:
            count,word = queue.popleft()
            
            
            for c in "abcdefghijklmnopqrstuvwxyz":
                for i in range(n):
                    new_word = word[:i]+c+word[i+1:]

                    if new_word == beginWord:
                        return count+1

                    if new_word in words and new_word not in visited:
                        queue.append((count+1,new_word))
                        visited.add(new_word)


        return 0        