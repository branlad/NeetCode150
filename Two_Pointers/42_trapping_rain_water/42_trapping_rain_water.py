class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        # initialize two pointers
        l, r = 0, len(height) - 1

        # initialize leftMax and rightMax to the first and last heights in the array, respectively
        # these are the max heights to the left and right of the current index
        leftMax = height[0]
        rightMax = height[-1]

        # initialize result
        res = 0

        while l < r:
            # if leftMax is smaller than rightMax, move left pointer to the right by 1
            if leftMax < rightMax:
                l += 1
                # update leftMax
                leftMax = max(leftMax, height[l])
                # if current height was greater than the previous leftMax, then 0 water will be stored
                res += leftMax - height[l]

            # if rightMax is smaller than leftMax or they are equal, move right pointer to the left by 1
            else:
                r -= 1
                # update rightMax
                rightMax = max(rightMax, height[r])
                # if current height was greater than the previous rightMax, then 0 water will be stored
                res += rightMax - height[r]

        return res
