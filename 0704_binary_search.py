class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)
    
    def binary_search(self, nums, left, right, target) -> int:
        if left > right or left < 0 or right >= len(nums):
            return -1
        else:
            center = int((left + right) / 2)
            
            return center if nums[center] == target else max(self.binary_search(nums, left, center - 1, target), self.binary_search(nums, center + 1, right, target))
