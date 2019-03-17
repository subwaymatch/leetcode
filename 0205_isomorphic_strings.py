class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        
        if len(s) != len(t):
            return False

        for idx in range(len(s)):
            s_char = s[idx]
            t_char = t[idx]
            
            if s_char not in s_dict:
                s_dict[s_char] = t_char
            elif s_dict[s_char] != t_char:
                return False
            
            if t_char not in t_dict:
                t_dict[t_char] = s_char
            elif t_dict[t_char] != s_char:
                return False
        
        return True
