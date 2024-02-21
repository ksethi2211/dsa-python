class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def bk(path: List[int]):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for num in nums:
                if not num in path:
                    path.append(num)
                    bk(path)
                    path.pop()
            
        bk([])
                
        return result