# https://leetcode.com/problems/two-out-of-three/description/
# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

# Example 1:

# Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
# Output: [3,2]
# Explanation: The values that are present in at least two arrays are:
# - 3, in all three arrays.
# - 2, in nums1 and nums2.
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
# --- My solution
class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        n1, n2, n3 = set(nums1), set(nums2), set(nums3)
        c = {}

        for n in [n1,n2,n3]:
            for x in n:
                c[x] = c.get(x, 0) + 1
        
        return [x for x, y in c.items() if y >= 2]

# --- Test
sol = Solution()
print(sol.twoOutOfThree(nums1, nums2, nums3))