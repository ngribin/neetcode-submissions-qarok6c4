class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for w in words:
            flag = 1
            for ch in w:
                if ch not in allowed:
                    flag = 0
            count += flag

        return count