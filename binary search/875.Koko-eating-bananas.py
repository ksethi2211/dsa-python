class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isFeasible(speed: int) -> bool:
            result = 0
            for pile in piles:
                result += math.ceil(pile / speed)
                if result > h:
                    return False
            return True

        lower = 1
        upper = max(piles)

        while lower <= upper:
            mid = (lower + upper) // 2
            is_mid_feasible = isFeasible(mid)

            if is_mid_feasible and (mid == 1 or (not isFeasible(mid - 1))):
                return mid
            if is_mid_feasible:
                upper = mid - 1
            else:
                lower = mid + 1