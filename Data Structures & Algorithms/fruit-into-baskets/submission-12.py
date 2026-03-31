class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        left = 0
        for i in range(len(fruits)):
            counts[fruits[i]] += 1

            if len(counts) > 2:
                counts[fruits[left]] -= 1
                if counts[fruits[left]] == 0:
                    counts.pop(fruits[left])
                left += 1

        return len(fruits) - left