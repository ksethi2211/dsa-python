class Solution:
    def isHappy(self, n: int) -> bool:
        def getNextNum(n: int) -> int:
            n_as_str = f"{n}"
            result = 0
            for c in n_as_str:
                result += (int(c) * int(c))
            return result

        visited = set()
        while True:
            if n in visited:
                return False
            if n == 1:
                return True
            visited.add(n)
            n = getNextNum(n)