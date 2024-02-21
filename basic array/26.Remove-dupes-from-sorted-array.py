class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currentPosPtr = 1
        nonDupePtr = 1
        while True:
            if nonDupePtr == len(nums):
                break
            if nums[nonDupePtr] == nums[nonDupePtr - 1]:
                nonDupePtr += 1
            else:
                if currentPosPtr != nonDupePtr:
                    nums[currentPosPtr] = nums[nonDupePtr]
                nonDupePtr += 1
                currentPosPtr += 1
        return currentPosPtr