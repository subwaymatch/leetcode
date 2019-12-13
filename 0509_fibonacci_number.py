class Solution:
    def fib(self, N: int) -> int:
        if N == 0: 
            return 0
        
        fib_lookup = []
        
        fib_lookup.append(0)
        fib_lookup.append(1)
        
        for i in range(2, N + 1):
            fib_lookup.append(fib_lookup[i - 1] + fib_lookup[i - 2])
        
        return fib_lookup[-1]
