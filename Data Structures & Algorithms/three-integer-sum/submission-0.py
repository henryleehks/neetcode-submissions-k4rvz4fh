class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate i

            start, end = i + 1, len(nums) - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total == 0:
                    res.append([nums[i], nums[start], nums[end]])

                    # skip duplicates for start and end
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1

                    start += 1
                    end -= 1
                elif total < 0:
                    start += 1
                else:
                    end -= 1

        return res
