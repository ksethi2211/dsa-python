class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityEl = 0
        majorityElCount = 0
        for item in nums:
            if majorityElCount == 0:
                majorityEl = item
                majorityElCount = 1
            elif item == majorityEl:
                majorityElCount += 1
            else:
                majorityElCount -= 1

        return majorityEl