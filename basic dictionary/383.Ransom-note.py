class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        for c in magazine:
            if c in magazine_dict:
                magazine_dict[c] += 1
            else:
                magazine_dict[c] = 1
        
        for c in ransomNote:
            if c in magazine_dict:
                magazine_dict[c] -= 1
                if magazine_dict[c] < 0:
                    return False
            else:
                return False
        
        return True