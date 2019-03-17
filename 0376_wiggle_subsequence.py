class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp_inc = [1] * len(nums) 
        dp_des = [1] * len(nums)
        top_idx = 0
        btm_idx = 0

        for idx in range(1, len(nums)):
            new_top_idx = top_idx
            new_btm_idx = btm_idx

            if nums[idx] > nums[btm_idx]:
                dp_inc[idx] = 1 + dp_des[btm_idx]
                new_top_idx = idx
            else:
                dp_inc[idx] = max(dp_inc[idx - 1], dp_des[idx - 1])

            if nums[idx] < nums[top_idx]:
                dp_des[idx] = 1 + dp_inc[top_idx]
                new_btm_idx = idx
            else:
                dp_des[idx] = max(dp_inc[idx - 1], dp_des[idx - 1])
            
            top_idx = new_top_idx
            btm_idx = new_btm_idx

        return max(dp_inc[-1], dp_des[-1])
