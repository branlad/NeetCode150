class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

            res = max(res, area)

        return res
