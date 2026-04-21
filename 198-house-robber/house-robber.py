class Solution:
    def rob(self, nums: List[int]) -> int:
        #если всего один дом
        if len(nums) == 1:
            return nums[0]
        #dp[i] это максимум денег, который можно получить до i-го дома
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            #либо не грабит текущий дом
            #либо грабит его и добавляет к dp[i-2]
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]        