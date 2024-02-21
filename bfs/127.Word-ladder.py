class Solution:
    def getPatterns(self, word: str) -> List[str]:
        patterns = []
        for i in range(len(word)):
            pattern = word[0:i] + "*" + word[i+1:]
            patterns.append(pattern)
        return patterns

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0

        pattern_meta = {}
        for word in wordList:
            patterns = self.getPatterns(word)
            for pattern in patterns:
                if pattern in pattern_meta:
                    pattern_meta[pattern].append(word)
                else:
                    pattern_meta[pattern] = [word]
        
        word_que = deque()
        word_que.append(beginWord)
        result = 1

        visited = set()
        visited.add(beginWord)

        while word_que:
            result += 1
            current_level_length = len(word_que)
            for _ in range(current_level_length):
                current_word = word_que.popleft()
                patterns = self.getPatterns(current_word)
                for pattern in patterns:
                    if pattern in pattern_meta:
                        for w in pattern_meta[pattern]:
                            if w == endWord:
                                return result
                            if not w in visited:
                                word_que.append(w)
                                visited.add(w)

        return 0