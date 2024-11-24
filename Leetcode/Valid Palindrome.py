import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerString = s.lower()
        left = 0
        right =l en(b)-1
        while left < right:
            if not lowerString[left].isalnum():
                left += 1
            if not lowerString[right].isalnum():
                right -= 1
            if lowerString[right].isalnum() and lowerString[left].isalnum():
                if lowerString[left] != lowerString[right]:
                    return False
                right -=1
                left += 1
        return True
        
