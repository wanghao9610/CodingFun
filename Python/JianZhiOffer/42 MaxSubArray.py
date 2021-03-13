"""输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。"""

# dp problem, dp[i] = dp[i - 1] + num[i](num[i] > 0) or dp[i] = dp[i - 1] (num[i] <= 0)
# Time: O(n), Space: O(1) (in-place)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return
        m = nums[0]
        n = len(nums)
        for i in range(1, n):
            nums[i] += max(nums[i - 1], 0)
            if nums[i] > m:
                m = nums[i]
        return max(nums)