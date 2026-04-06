class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num+1):
            sq = i * i
            if sq == num:
                return True
        return False