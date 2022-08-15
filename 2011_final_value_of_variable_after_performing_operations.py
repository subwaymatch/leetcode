class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        final_value = 0
        
        for op in operations:
            final_value = final_value + 1 if op[1] == "+" else final_value - 1
            
        return final_value
