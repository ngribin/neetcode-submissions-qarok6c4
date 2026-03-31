"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_df = sorted([i.start for i in intervals])
        end_df = sorted([i.end for i in intervals])
        count = 0
        res = 0
        s, e = 0, 0

        while s < len(start_df):
            if start_df[s] < end_df[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
            
        return res
            