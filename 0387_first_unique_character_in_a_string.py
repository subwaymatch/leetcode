class Solution:
    def firstUniqChar(self, s: str) -> int:
        first_indices = {}
        duplicates = {}

        for idx, c in enumerate(s):
            if c not in duplicates: 
                if c in first_indices:
                    first_indices.pop(c)
                    duplicates[c] = True
                
                else:
                    first_indices[c] = idx

        if len(first_indices) == 0:
            return -1
        
        return sorted(first_indices.items(), key=lambda x: x[1])[0][1]
