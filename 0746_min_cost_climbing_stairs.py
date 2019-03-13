class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        elif len(cost) == 1:
            return cost[0]
        
        for idx in range(2, len(cost)):
            cost[idx] += min(cost[idx - 1], cost[idx - 2])
        
        return min(cost[-2:])
