class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0

        for idx in range(len(nums)):
            if nums[idx] == 0:
                zero_count += 1
            elif zero_count > 0:
                nums[idx - zero_count] = nums[idx]

        for idx in range(zero_count):
            nums[-idx - 1] = 0
