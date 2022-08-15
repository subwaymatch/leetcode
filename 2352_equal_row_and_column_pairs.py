class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trie_dict = {}
        
        # add each column to trie
        for j in range(n):
            previous_node = trie_dict
            
            for i in range(n):
                num = grid[i][j]
                
                if num not in previous_node:
                    previous_node[num] = {}
                
                previous_node = previous_node[num]
            
            if "count" not in previous_node:
                previous_node["count"] = 1
            else:
                previous_node["count"] += 1
                
        num_equal_pairs = 0
        
        # iterate over each row and check if a path exists in trie
        # if a path exists, increment the counter by the matching count
        for i in range(n):
            previous_node = trie_dict
            
            for j in range(n):
                num = grid[i][j]
                
                if num not in previous_node:
                    break
                
                previous_node = previous_node[num]
            
            if "count" in previous_node:
                num_equal_pairs += previous_node["count"]
        
        return num_equal_pairs
