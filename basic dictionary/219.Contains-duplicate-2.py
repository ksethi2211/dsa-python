class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_meta = {}

        for i in range(len(nums)):
            if nums[i] in nums_meta:
                if i - nums_meta[nums[i]] <= k:
                    return True
            nums_meta[nums[i]] = i

        return False