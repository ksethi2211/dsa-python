class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        visited = set()
        prev = None
        for num in nums:
            if prev == num:
                continue
            if (target - num) in visited:
                prev = num
                result.append([target - num, num])
            else:
                visited.add(num)
    
        return result
                

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        prev = None
        result = []
        for i in range(len(nums)):
            num = nums[i]
            if num == prev: 
                continue
            twoSumResult = self.twoSum(nums[i+1:], -1 * num)
            for res in twoSumResult:
                res.insert(0, num)
                result.append(res)
            prev = num
        return result