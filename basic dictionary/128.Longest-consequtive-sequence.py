class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        
        memoized_set = set()
        result = 0
        for num in nums:
            if num in memoized_set or num - 1 in nums_set:
                continue
            current_result = 1
            n = num + 1
            while n in nums_set:
                current_result += 1
                n += 1
            result = max(result, current_result)
            memoized_set.add(num)
            
        return result