class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if (len(s) != len(goal)) or (len(s) <= 1):
            return False
        
        diff_count = 0
        diff_1 = None
        diff_2 = None
        
        for i in range(len(s)):
            if s[i] !=  goal[i]:
                if diff_count == 0:
                    diff_1 = s[i]
                    diff_2 = goal[i]
                    diff_count += 1
                    
                elif diff_count == 1:
                    
                    if (diff_1 != goal[i]) or (diff_2 != s[i]):
                        return False
                    
                    diff_count += 1
                
                else:
                    return False
                
        if diff_count == 0:
            char_count_dict = {}
            
            for c in s:
                if c not in char_count_dict:
                    char_count_dict[c] = 0
                
                char_count_dict[c] += 1
                if char_count_dict[c] > 1:
                    return True
                
            return False
        else:
            return diff_count == 2
