"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start_num = sorted([x.start for x in intervals ])
        end_num = sorted([x.end for x in intervals ])
        res = 0
        count = 0

        left, right = 0, 0

        while left < len(start_num):
            if start_num[left] < end_num[right]:
                count += 1
                left += 1
            else:
                count -= 1
                right += 1

            res = max(res, count)

        return res