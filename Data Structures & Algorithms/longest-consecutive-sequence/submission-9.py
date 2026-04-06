class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        res = []
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if i == len(nums) - 1:
                    res.append(count)
                else:
                    continue
            elif nums[i] - nums[i-1] == 1:
                count += 1
                if i == len(nums) - 1:
                    res.append(count)
            else:
                res.append(count)
                count = 1
        
        if len(res) == 0: 
            return 1

        return max(res)