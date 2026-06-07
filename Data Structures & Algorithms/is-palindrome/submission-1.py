class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringa = "".join(i.lower() for i in s if i.isalnum())
        stringb = "".join(s[i].lower() for i in range(len(s) - 1 , -1 , -1) if s[i].isalnum())
        return stringa == stringb