class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp[i] это минимальное количество монет для суммы i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  #чтобы собрать 0, нужно 0 монет
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    #берет текущую монету и смотрит лучшее решение для остатка
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        #если значение не изменилось, то собрать сумму невозможно
        return dp[amount] if dp[amount] != float('inf') else -1