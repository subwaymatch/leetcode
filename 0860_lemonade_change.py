class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_bills = {
            5: 0, 
            10: 0, 
            20: 0
        }
        
        for bill in bills:
            if bill == 5:
                num_bills[5] += 1
            elif bill == 10:
                num_bills[5] -= 1
                num_bills[10] += 1
            else:
                if num_bills[10] > 0:
                    num_bills[10] -= 1
                    num_bills[5] -= 1
                else:
                    num_bills[5] -= 3
                    
            if num_bills[5] < 0 or num_bills[10] < 0:
                return False
        
        return True
