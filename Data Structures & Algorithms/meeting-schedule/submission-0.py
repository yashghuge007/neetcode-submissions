"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        inter = sorted(intervals,key=lambda x:x.start)
        for i in range(1,n):
            if inter[i].start<inter[i-1].end:
                return False
        return True
