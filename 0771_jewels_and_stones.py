class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_dict = {}
        jewel_count = 0
        
        for jewel in J:
            jewel_dict[jewel] = True
            
        for stone in S:
            if stone in jewel_dict:
                jewel_count += 1
            
        return jewel_count
