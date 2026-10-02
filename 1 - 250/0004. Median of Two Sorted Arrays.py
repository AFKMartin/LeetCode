# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
nums1 = [1, 2]
nums2 = [3, 4]
# Using binary search to solve it on O(log (m+n)), maybe there is a better simplier version but I'm tired of trying stuff 😔
# --- My solution
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        l1, l2 = nums1, nums2
        if len(l1) > len(l2):
            l1, l2 = l2, l1
        
        m , n = len(l1), len(l2)
        lt = m + n
        half = lt//2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  
            j = half - i

            Aleft = l1[i - 1] if i > 0 else float("-infinity")
            Aright = l1[i] if i < m else float("infinity")

            Bleft = l2[j - 1] if j > 0 else float("-infinity")
            Bright = l2[j] if j < n else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if lt % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1                   

# --- Test 
sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))