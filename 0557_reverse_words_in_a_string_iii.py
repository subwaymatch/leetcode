class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = ""
        
        for word in words:
            result += word[::-1] + " "
        
        return result[:-1]
