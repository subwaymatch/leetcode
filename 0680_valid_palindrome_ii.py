class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.isValidPalindrome(s, False)
    
    def isValidPalindrome(self, s: str, did_delete: bool) -> bool:
        curr_left = 0
        curr_right = len(s) - 1
        
        while curr_left < curr_right:
            # If left and right characters are same, keep checking
            if s[curr_left] == s[curr_right]:
                curr_left += 1
                curr_right -= 1
            # If already deleted, not a valid palindrome
            elif did_delete:
                return False
            # If we can still delete one character,
            # run check after deleting left, right character
            else:
                return self.isValidPalindrome(s[curr_left + 1:curr_right + 1], True) or self.isValidPalindrome(s[curr_left:curr_right], True)
                
        return True
