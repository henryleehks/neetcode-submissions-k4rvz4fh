class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        new_s = ''.join(char for char in s if char.isalnum())
        for i in range(len(new_s)//2):
            front = new_s[i]
            back = new_s[-i-1]
            if front != back:
                return False
        return True