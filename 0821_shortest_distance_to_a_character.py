class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        shortest_distances = [0] * len(S)
        C_locations = [idx for idx, char in enumerate(S) if char == C]
        
        # Leftmost/rightmost
        for i in range(0, C_locations[0]):
            shortest_distances[i] = C_locations[0] - i
        
        for i in range(C_locations[-1] + 1, len(S)):
            shortest_distances[i] = i - C_locations[-1]
            
        for i in range(0, len(C_locations) - 1):
            num_elements_in_between = C_locations[i + 1] - C_locations[i] - 1
            half = int(num_elements_in_between / 2)
            is_odd = num_elements_in_between % 2 != 0
            
            for j in range(1, half + 1):
                shortest_distances[C_locations[i] + j] = j
                shortest_distances[C_locations[i + 1] - j] = j
                
            if is_odd:
                shortest_distances[C_locations[i] + half + 1] = half + 1
        
        return shortest_distances
