class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)    
        #если сумма нечетная, то сразу невозможно
        if total % 2 != 0:
            return False
        target = total // 2
        #dp[i] это можно ли набрать сумму i
        dp = [False] * (target + 1)
        dp[0] = True  #сумму 0 всегда можно набрать
        for num in nums:
            #идет с конца, чтобы не использовать элемент несколько раз
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
        return dp[target]