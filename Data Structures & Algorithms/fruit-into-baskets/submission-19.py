class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        h = defaultdict(int)
        left = 0
        for i in range(len(fruits)):
            h[fruits[i]] += 1

            if len(h) > 2:
                h[fruits[left]] -= 1
                if h[fruits[left]] == 0:
                    del h[fruits[left]]
                left += 1 

        return len(fruits) - left