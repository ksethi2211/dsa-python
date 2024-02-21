class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_len = len(s)
        s_dict = {}
        t_set = set()
        for i in range(s_len):
            s_char = s[i]
            t_char = t[i]

            if (s_char in s_dict) and (s_dict[s_char] != t_char):
                return False
            if  not (s_char in s_dict) and (t_char in t_set):
                return False
            s_dict[s_char] = t_char
            t_set.add(t_char)
        
        return True