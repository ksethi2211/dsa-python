"""
    1 1 1 2 2 2 3
    1 1 1 2 2 2 3
    1 1 2 2 
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currentPosPtr = 0
        currentElCount = 0
        nonDupePtr = 0
        while True:
            if nonDupePtr == len(nums):
                break
            
            if nonDupePtr == 0 or nums[nonDupePtr] != nums[nonDupePtr - 1]:
                currentElCount = 1
            else:
                currentElCount += 1
            
            if currentElCount <= 2:
                nums[currentPosPtr] = nums[nonDupePtr]
                currentPosPtr += 1
                nonDupePtr += 1
            else:
                nonDupePtr += 1

        return currentPosPtr
                
