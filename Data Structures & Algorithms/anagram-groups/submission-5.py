class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for letter in strs:
            sortedS = "".join(sorted(letter))
            seen[sortedS].append(letter)

        return list(seen.values())    
        