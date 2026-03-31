import bisect
class TimeMap:

    def __init__(self):
        self.data = defaultdict(lambda: ([], []))
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        ts, vs = self.data[key]

        ts.append(timestamp)
        vs.append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        ts, vs = self.data[key]
        idx = bisect.bisect_right(ts, timestamp) - 1

        return vs[idx] if idx >= 0 else ""