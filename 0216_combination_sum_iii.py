class Solution:
    def __init__(self):
        self.combinations = []
        self.n = 0
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.n = n
        self.find_combinations(k, 1, [], 0)
        return self.combinations
    
    def find_combinations(self, k_left: int, start_num: int, current_combination: List[int], current_sum: int) -> None:
        if k_left == 0 and current_sum == self.n:
            self.combinations.append(current_combination.copy())
            return
        
        for num in range(start_num, 10):
            new_sum = current_sum + num
            
            if new_sum > self.n:
                return
            else:
                current_combination.append(num)
                
                self.find_combinations(k_left - 1, num + 1, current_combination, new_sum)
                
                current_combination.pop()
