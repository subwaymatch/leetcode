class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        prev_one_stream = -1
        curr_one_stream = 0
        
        for n in nums:
            if n == 1:
                curr_one_stream += 1
            else:
                temp = prev_one_stream + 1 + curr_one_stream
                max_ones = max_ones if max_ones > temp else temp
                
                prev_one_stream = curr_one_stream
                curr_one_stream = 0
                
        temp = prev_one_stream + 1 + curr_one_stream
        max_ones = max_ones if max_ones > temp else temp
        
        return max_ones
