class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for word in words:
            flag = 1
            for ch in word:
                if ch not in allowed:
                    flag = 0
                    break
                    
                    
              
            count += flag
           
        return count