class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        new_s = ''.join(ch for ch in s if ch.isalnum())

        for i in range(len(new_s)//2):
            if new_s[i] != new_s[-i-1]:
                return False

        return True