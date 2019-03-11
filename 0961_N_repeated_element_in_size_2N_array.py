class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        seenDict = {}
        
        for num in A:
            if num in seenDict:
                return num
            else:
                seenDict[num] = True
