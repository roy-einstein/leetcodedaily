from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        one_step = self.climbStairs(n - 1)
        two_step = self.climbStairs(n - 2)
        return one_step + two_step

    @cache
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        one_step = self.climbStairs(n - 1)
        two_step = self.climbStairs(n - 2)
        return one_step + two_step