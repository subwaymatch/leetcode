class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        
        size_idx = 0
        greed_idx = 0
        count = 0
        
        while greed_idx != len(g) and size_idx != len(s):
            if g[greed_idx] <= s[size_idx]:
                count = count + 1
                greed_idx = greed_idx + 1
                size_idx = size_idx + 1
            
            else:
                size_idx = size_idx + 1
        
        return count
