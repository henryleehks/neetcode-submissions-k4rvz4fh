class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tmp = []
        for num in nums:
            # If num = val, skip
            if num == val:
                continue
            # If num != val, append to tmp list
            tmp.append(num)
            # len(tmp) == k
        for i in range(len(tmp)):
            # replace first k elements in nums with tmp[i]
            nums[i] = tmp[i]
        return len(tmp)