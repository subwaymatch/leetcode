class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        did_modify = nums[0] > nums[1]
        
        for i in range(2, len(nums)):
            if nums[i - 1] > nums[i]:
                if did_modify:
                    return False
                else: 
                    if nums[i] >= nums[i - 2]:
                        nums[i - 1] = nums[i - 2]
                    else:
                        nums[i] = nums[i - 1]
                        
                    did_modify = True
                    
        return True
