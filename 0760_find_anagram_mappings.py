class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        order_map = {}
        order_list = []
        
        for idx, num in enumerate(B):
            order_map[num] = idx
            
        for num in A:
            order_list.append(order_map[num])
        
        return order_list
