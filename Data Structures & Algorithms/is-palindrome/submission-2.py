class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = "".join(char.lower() for char in s if char.isalnum())
        return palindrome == palindrome[::-1]
