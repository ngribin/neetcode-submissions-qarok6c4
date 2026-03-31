class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for det in details:
            phone = det[:11]
            age = det[-4:-2]
            if int(age) > 60:
                count += 1
        return count
        