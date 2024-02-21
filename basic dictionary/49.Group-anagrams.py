class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_dict = {}

        for str in strs:
            sorted_str = ''.join(sorted(str))
            print(sorted_str)
            if sorted_str in words_dict:
                words_dict[sorted_str].append(str)
            else:
                words_dict[sorted_str] = [str]
        
        return words_dict.values()