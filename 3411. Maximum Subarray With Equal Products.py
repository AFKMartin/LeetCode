# https://leetcode.com/problems/maximum-subarray-with-equal-products/description/
# You are given an array of positive integers nums.
# An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:
# prod(arr) is the product of all elements of arr.
# gcd(arr) is the GCD of all elements of arr.
# lcm(arr) is the LCM of all elements of arr.
# Return the length of the longest product equivalent subarray of nums.

# Example 1:

# Input: nums = [1,2,1,2,1,1,1]
# Output: 5
# Explanation: 
# The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.
nums = [1, 2, 1, 1, 1]
# --- My solution
class Solution:
    def maxLength(self, nums) -> int:
        # gcd(a,b)⋅lcm(a,b)=a⋅b
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a 
        def lcm(a, b):
            return (a * b) // gcd(a, b)
        
        max_len = 0
        n = len(nums)

        for i in range(n):
            prod = nums[i] 
            g = nums[i] 
            l = nums[i] 
            if prod == g * l: 
                max_len = max(max_len, 1) 

            for j in range(i + 1, n): 
                prod *= nums[j] 
                g = gcd(g, nums[j]) 
                l = lcm(l, nums[j]) 
            
                if prod == g * l: 
                    max_len = max(max_len, j - i + 1)
                else:
                    break
        
        return max_len
            
# --- Test
sol = Solution()
print(sol.maxLength(nums))
