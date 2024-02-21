class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        s_set = set()
        pattern_len = len(pattern)
        s_list = s.split(" ")
        s_len = len(s_list)

        if(s_len != pattern_len):
            return False
        
        for i in range(pattern_len):
            if pattern[i] in pattern_dict and pattern_dict[pattern[i]] != s_list[i]:
                return False
            if (not (pattern[i] in pattern_dict)) and (s_list[i] in s_set):
                return False
            pattern_dict[pattern[i]] = s_list[i]
            s_set.add(s_list[i])
        
        return True
