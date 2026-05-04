class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lenth = len(nums)
        sum = 0
        for i in range(0, len(nums)):
            sum = sum + nums[i]
        total = lenth * (lenth + 1) / 2
        return int(total - sum)