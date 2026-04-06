class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = {}
        for c in s1:
            s1_set[c] = s1_set.get(c, 0) + 1
        
        l = 0
        r = len(s1)

        while r < len(s2) + 1:
            window = s2[l:r]
            window_set = {}
            for c in window:
                window_set[c] = window_set.get(c, 0) + 1
            if s1_set == window_set:
                return True
            l +=1
            r += 1

        return False