class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set()
        dict1 = { i: 1 for i in nums1 }
        for n in nums2:
            if n in dict1:
                intersection.add(n)
        
        return list(intersection)
