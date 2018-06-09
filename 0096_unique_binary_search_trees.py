class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        num_bst_list = [1]
        
        return self.numTreeDP(n, num_bst_list)
    
        
    def numTreeDP(self, n, num_bst_list):
        # If n doesn't exist in dp table, recursively count it
        if len(num_bst_list) <= n:
            count = 0
            
            for parent in range(n // 2):
                parent = parent + 1
                
                count = count + (self.numTreeDP(parent - 1, num_bst_list) * self.numTreeDP(n - parent, num_bst_list)) * 2
                
            if (n % 2 == 1):
                count = count + pow(self.numTreeDP(n // 2, num_bst_list), 2)
        
            num_bst_list.append(count)
        
        
        return num_bst_list[n]
