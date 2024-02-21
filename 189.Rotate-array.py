class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        requiredRotations = k % len(nums)
        if requiredRotations == 0:
            return
        
        def reverse(startIdx: int, endIdx: int) -> None:
            while startIdx < endIdx:
                nums[startIdx], nums[endIdx] = nums[endIdx], nums[startIdx]
                startIdx += 1
                endIdx -= 1
        
        reverse(0, len(nums) - 1)
        reverse(0, requiredRotations - 1)
        reverse(requiredRotations, len(nums) - 1)