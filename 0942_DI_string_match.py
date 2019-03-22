class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        inc = 0
        dec = len(S)
        output = []
        
        for c in S:
            if c == 'I':
                output.append(inc)
                inc += 1
            else:
                output.append(dec)
                dec -= 1
        
        output.append(inc if S[-1] == 'I' else dec)
        
        return output
