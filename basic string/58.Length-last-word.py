class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped_str = s.strip()
        str_arr = stripped_str.split(" ")
        
        return len(str_arr[len(str_arr) - 1])