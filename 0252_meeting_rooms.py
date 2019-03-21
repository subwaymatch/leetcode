# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals_sorted = sorted(intervals, key=lambda i: i.start)
       
        for i in range(1, len(intervals_sorted)):
            if intervals_sorted[i].start < intervals_sorted[i - 1].end:
                return False
        
        return True
