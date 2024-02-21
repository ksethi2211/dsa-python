"""
    4 5 6 7 8 9 10 0 1 2

    mid > low and mid < hi
        pivot after mid
        if target between mid and low
            upper = mid - 1
    else
        pivot before mid
            if target between mid and high
            upper = mid + 1
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while lower <= upper:
            mid = (lower + upper) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[lower] and nums[mid] > nums[upper]:
                if nums[lower] <= target and target < nums[mid]:
                    upper = mid - 1
                else:
                    lower = mid + 1
            else:
                if nums[mid] < target and target <= nums[upper]:
                    lower = mid + 1
                else:
                    upper = mid - 1
        
        return -1
        