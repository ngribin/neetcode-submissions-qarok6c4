class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        count = 0
        res = float("inf")

        for right in range(len(blocks)):
            if blocks[right] == "W":
                count += 1

            while right - left + 1 == k:
                res = min(res, count)
                if blocks[left] == "W":
                    count -= 1
                left += 1
        return res