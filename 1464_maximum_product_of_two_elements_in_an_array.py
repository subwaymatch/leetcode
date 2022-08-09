class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = nums[0] if nums[0] > nums[1] else nums[1]
        second_largest = nums[1] if nums[0] > nums[1] else nums[0]
        
        for num in nums[2:]:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest:
                second_largest = num
                
        return (largest - 1) * (second_largest - 1)
