class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        while True:
            if len(prefix) == len(strs[0]):
                break
            
            toBreak = False
            currentChar = strs[0][len(prefix)]
            for word in strs:
                if len(word) == len(prefix) or word[len(prefix)] != currentChar:
                    toBreak = True
                    break
            if toBreak:
                break
            prefix = f"{prefix}{currentChar}"
        
        return prefix
