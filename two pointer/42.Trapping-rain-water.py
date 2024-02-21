class Solution:
    def trap(self, height: List[int]) -> int:
        lower = 0
        upper = len(height) - 1
        lowerHeight = 0
        upperHeight = 0
        res = 0

        while lower <= upper:
            if height[lower] > lowerHeight:
                lowerHeight = height[lower]
                lower += 1
                continue

            if height[upper] > upperHeight:
                upperHeight = height[upper]
                upper -= 1
                continue
            
            if lowerHeight < upperHeight:
                res += lowerHeight - height[lower]
                lower += 1
            else:
                res += upperHeight - height[upper]
                upper -= 1
        
        return res

