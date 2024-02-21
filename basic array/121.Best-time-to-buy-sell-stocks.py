class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        isMinSet = False
        isMaxSet = False
        minPrice = 0
        maxPrice = 0
        result = 0
        for price in prices:
            if not isMinSet or minPrice > price:
                isMinSet = True
                minPrice = price
                isMaxSet = False
                maxPrice = 0
            elif not isMaxSet or maxPrice < price:
                isMaxSet = True
                maxPrice = price
            
            if isMaxSet:
                result = max(result, maxPrice - minPrice)
    
        return result
