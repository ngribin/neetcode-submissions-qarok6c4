class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        count = Counter(s1)
        window = Counter(s2[:len1])

        if count == window:
            return True

        for i in range(len1, len2):
            window[s2[i]] += 1
            window[s2[i-len1]] -= 1

            if window[s2[i-len1]] == 0:
                del window[s2[i-len1]]

            
            if window == count:
                return True

        return False