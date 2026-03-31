class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            h[sortedS].append(s)

        return list(h.values())    