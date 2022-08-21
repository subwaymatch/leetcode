class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count_dict = {}
        
        for num in arr:
            if num not in count_dict:
                count_dict[num] = 0
            
            count_dict[num] += 1
            
        count_arr = list(count_dict.values())
        count_arr.sort()
        
        removed_count = 0
        
        for i in count_arr:
            if k >= i:
                removed_count += 1
                k -= i
            else:
                break
                
        return len(count_arr) - removed_count
