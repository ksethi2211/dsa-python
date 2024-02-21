class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        
        if s_len != t_len:
            return False
        
        s_dict = {}
        for i in range(s_len):
            char_code = ord(s[i])
            if char_code in s_dict:
                s_dict[char_code] += 1
            else:
                s_dict[char_code] = 1
        
        for i in range(s_len):
            char_code = ord(t[i])
            if char_code in s_dict:
                s_dict[char_code] -= 1
                if s_dict[char_code] < 0:
                    return False
            else:
                return False

        return True
