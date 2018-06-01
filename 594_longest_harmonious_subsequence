class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        max_count = 0
        
        for num in nums: 
            if num in dict:
                dict[num] = dict[num] + 1
            
            else:
                dict[num] = 1
        
        for num, count in dict.items(): 
            if num + 1 in dict:
                sub_count = count
                sub_count = sub_count + dict[num + 1]
            
                max_count = max(max_count, sub_count)
            
        return max_count
