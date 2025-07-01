# https://leetcode.com/problems/type-of-triangle/description/
# You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.
# A triangle is called equilateral if it has all sides of equal length.
# A triangle is called isosceles if it has exactly two sides of equal length.
# A triangle is called scalene if all its sides are of different lengths.
# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

# Example 1:

# Input: nums = [3,3,3]
# Output: "equilateral"
# Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.
nums = [3,3,3]
# --- My solution
# a + b > c (triangle)
class Solution:
    def triangleType(self, nums) -> str:
        a, b, c = sorted(nums)
        return "none" if a + b <= c else ["scalene", "isosceles", "equilateral"][3 - len(set(nums))]
# --- Test 
sol = Solution()
print(sol.triangleType(nums))
