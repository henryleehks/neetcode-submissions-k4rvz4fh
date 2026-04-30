class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = Counter(s1)
        s2_set = {}

        l = 0
        r = len(s1)

        while r < len(s2) + 1:
            s2_set = Counter(s2[l:r])
            if s1_set == s2_set:
                return True
            l += 1
            r += 1
        return False