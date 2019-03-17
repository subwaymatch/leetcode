class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []

        if len(nums) == 1:
            ranges = [[nums[0], nums[0]]]
        elif len(nums) >= 2:
            new_range = [nums[0]]
            prev_num = nums[0]

            for idx in range(1, len(nums)):
                if nums[idx] != prev_num + 1:
                    new_range.append(prev_num)
                    ranges.append(new_range)
                    
                    new_range = [nums[idx]]
                
                prev_num = nums[idx]

            new_range.append(nums[-1])
            ranges.append(new_range)
        
        return list(map(lambda r: str(r[0]) if r[0] == r[1] else str(r[0]) + '->' + str(r[1]), ranges))
