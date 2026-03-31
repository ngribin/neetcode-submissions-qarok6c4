class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            s_key = "".join(sorted(s))
            res[s_key].append(s)

        return list(res.values())
