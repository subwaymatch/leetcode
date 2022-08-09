class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        edge_map = {}
        
        for pair in adjacentPairs:
            if pair[0] not in edge_map:
                edge_map[pair[0]] = []
            if pair[1] not in edge_map:
                edge_map[pair[1]] = []
            
            edge_map[pair[0]].append(pair[1])
            edge_map[pair[1]].append(pair[0])
           
        prev_node = None
        current_node = next(filter(lambda i: len(i[1]) == 1, edge_map.items()))[0]
        l = []
        
        while current_node is not None:
            l.append(current_node)
            temp_node = current_node
            current_node = next(filter(lambda n: n != prev_node, edge_map[current_node]), None)
            prev_node = temp_node
            
        return l
