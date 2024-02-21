class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = []
        def bk(remaining_digits: str, path: List[str]):
            if len(remaining_digits) == 0:
                if len(path) != 0:
                    result.append("".join(path))
                return
            current_digit = remaining_digits[0]
            mapping = mapping_dict[current_digit]
            for c in mapping:
                path.append(c)
                bk(remaining_digits[1:], path)
                path.pop()

        bk(digits, [])
        return result
            