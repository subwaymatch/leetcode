class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_char1 = None
        diff_char2 = None
        diff_count = 0
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff_char1 is None:
                    diff_char1 = s1[i]
                    diff_char2 = s2[i]
                    diff_count += 1
                elif diff_count > 2:
                    return False
                elif (diff_char1 == s2[i]) and (diff_char2 == s1[i]):
                    diff_count += 1
                else:
                    return False
        
        return (diff_count == 0) or (diff_count == 2)
