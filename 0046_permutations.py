class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur_arr = []
        permutations = []
        
        self.permute_backtrack(nums, cur_arr, permutations)
        
        return permutations
        
    def permute_backtrack(self, nums, cur_arr, permutations):
        if len(nums) == len(cur_arr):
            permutations.append(cur_arr.copy())

        for idx in range(len(nums)):
            if nums[idx] not in cur_arr:
                cur_arr.append(nums[idx])
                self.permute_backtrack(nums, cur_arr, permutations)
                cur_arr.pop()
