class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        target_idx = 0
        target_char = s[0]

        for c in t:
            if c == target_char:
                target_idx += 1
                if target_idx == len(s):
                    return True

                target_char = s[target_idx]

        return False
