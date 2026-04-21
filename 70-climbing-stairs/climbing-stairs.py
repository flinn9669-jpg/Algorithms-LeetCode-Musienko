class Solution:
    def climbStairs(self, n: int) -> int:
        #базовые случаи
        if n == 1:
            return 1
        if n == 2:
            return 2     
        #dp[i] это количество способов добраться до i-й ступеньки
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        #заполняет массив по формуле
        for i in range(3, n + 1):
            #можно прийти либо с (i-1), либо с (i-2)
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]