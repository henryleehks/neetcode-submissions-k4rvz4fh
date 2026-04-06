class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        new_s = ''.join(char for char in s if char.isalnum())
        for i in range(len(new_s)//2):
            if new_s[i] != new_s[-i-1]:
                return False
        return True