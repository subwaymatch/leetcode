class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        left = 0
        right = len(nums) - 1
        
        while left != right:
            length = right - left + 1
            mid = int((right - left) / 2) + left

            if int(length / 2) % 2 == 0:
                if nums[mid - 1] == nums[mid]:
                    right = mid
                else:
                    left = mid

            else:
                if nums[mid - 1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return nums[left]
