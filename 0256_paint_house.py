class Solution:
    def __init__(self):
        self.RED = 0
        self.BLUE = 1
        self.GREEN = 2
        
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0: 
            return 0
        
        for idx in range(1, len(costs)):
            prev_min_costs = costs[idx - 1]
            
            costs[idx][self.RED] += min(prev_min_costs[self.BLUE], prev_min_costs[self.GREEN])
            costs[idx][self.BLUE] += min(prev_min_costs[self.RED], prev_min_costs[self.GREEN])
            costs[idx][self.GREEN] += min(prev_min_costs[self.RED], prev_min_costs[self.BLUE])
            
        min_cost = min(costs[-1])
        
        return min_cost
