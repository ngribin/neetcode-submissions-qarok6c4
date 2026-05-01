class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for w in words:
            flag = True
            for ch in w:
                if ch not in allowed:
                    flag = False
            
            count += flag

        return count