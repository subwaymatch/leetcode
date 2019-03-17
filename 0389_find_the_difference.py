class Solution:
    def findTheDifference(self, s, t):
        char_map = {}

        for c in s:
            if c not in char_map:
                char_map[c] = 0
            
            char_map[c] += 1
        
        for c in t:
            if c not in char_map:
                return c

            char_map[c] -= 1
            
            if char_map[c] == 0:
                char_map.pop(c)

        return None
