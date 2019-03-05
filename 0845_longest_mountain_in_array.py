class Solution:
    def __init__(self):
        self.uphill_count = 0
        self.downhill_count = 0
        self.longest = 0
        
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3: 
            return self.longest
        
        # Begin at index 1
        for i in range(1, len(A)):
            # If uphill
            if A[i] > A[i - 1]:
                if self.downhill_count > 0:
                    self.check_if_longest()
                    self.reset_count()
                
                self.uphill_count += 1

            # If downhill
            elif A[i] < A[i - 1]:
                self.downhill_count += 1

            # If flat
            else:
                self.check_if_longest()
                self.reset_count()
        
        # After full pass, check if the last mountain is the longest one
        self.check_if_longest()
        
        return self.longest
     
    # A helper function to check if the last mountain is the longest one
    def check_if_longest(self) -> None:
        if self.uphill_count > 0 and self.downhill_count > 0:
            new_length = self.uphill_count + self.downhill_count + 1
            
            if new_length > self.longest:
                self.longest = new_length
   
    # Reset uphill/downhill count
    def reset_count(self) -> None:
        self.uphill_count = 0
        self.downhill_count = 0
