class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = postfix = 1

        for i in range(len(nums)):
            res[i] = prefix # [1, 1, 2, 8]
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix # [64, 32, 16, 8]
            postfix *= nums[i] # 64

        return res