class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in visited_dict:
                return [visited_dict[target - num], i]
            visited_dict[num] = i