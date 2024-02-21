"""
    3, 3, 3, 3, 2, 5, 6, 3, 3
    2, 3, 3, 3, 3, 5, 6, 3, 3
    2, 5, 3, 3, 3, 3, 6, 3, 3
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        currentPositionPtr = 0
        nonValPtr = 0
        while True:
            if nonValPtr == len(nums):
                break
            if nums[nonValPtr] == val:
                nonValPtr += 1
                continue
            if nonValPtr != currentPositionPtr:
                nums[currentPositionPtr], nums[nonValPtr] = nums[nonValPtr], nums[currentPositionPtr]
            nonValPtr += 1
            currentPositionPtr += 1
        return currentPositionPtr
            
