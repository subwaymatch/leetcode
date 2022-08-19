class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            if s[i] == goal[0]:
                match = True
                
                for j in range(len(s)):
                    if s[(i + j) % len(s)] != goal[j]:
                        match = False
                        break
                
                if match:
                    return True
        
        return False
