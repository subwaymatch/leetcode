class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        result[-1] = nums[-1]
        running_product = 1

        for idx in reversed(range(1, len(nums) - 1)):
            result[idx] = nums[idx] * result[idx + 1]

        for idx in range(len(nums) - 1):
            result[idx] = running_product * result[idx + 1]
            running_product *= nums[idx]

        result[-1] = running_product

        return result
