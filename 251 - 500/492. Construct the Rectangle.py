# https://leetcode.com/problems/construct-the-rectangle/description
# A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
# The area of the rectangular web page you designed must equal to the given target area.
# The width W should not be larger than the length L, which means L >= W.
# The difference between length L and width W should be as small as possible.
# Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
# Example 1:

# Input: area = 4
# Output: [2,2]
# Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
# But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is # not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
area = 122122
# --- My solution
class Solution:
    def constructRectangle(self, area: int):
        s = int(area ** 0.5)
        while area % s != 0:
            s = s -1
        y = area // s
        if y > s:
            c = [y, s]
        else:
            c = [s, y]
        return c
# the last if is not needed, because "y" will always be higher or equal than "s"

# --- Test
sol = Solution()
print(sol.constructRectangle(area))