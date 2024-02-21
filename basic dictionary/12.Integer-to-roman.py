"""
    991
    CMXCI
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        mapping_dict = [
            {"val": 1000, "roman": "M"},
            {"val": 900, "roman": "CM"},
            {"val": 500, "roman": "D"},
            {"val": 400, "roman": "CD"},
            {"val": 100, "roman": "C"},
            {"val": 90, "roman": "XC"},
            {"val": 50, "roman": "L"},
            {"val": 40, "roman": "XL"},
            {"val": 10, "roman": "X"},
            {"val": 9, "roman": "IX"},
            {"val": 5, "roman": "V"},
            {"val": 4, "roman": "IV"},
            {"val": 1, "roman": "I"},
        ]

        result = ""
        while num > 0:
            current_roman = ""
            for item in mapping_dict:
                if item["val"] <= num:
                    current_roman = item["roman"]
                    num -= item["val"]
                    break;
            result = f"{result}{current_roman}"

        return result