class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_s = "".join(char.lower() for char in s if char.isalnum())
        return reversed_s == reversed_s[::-1]