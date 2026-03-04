# https://leetcode.com/problems/count-largest-group/description
# You are given an integer n.
# We need to group the numbers from 1 to n according to the sum of its digits. For example, the numbers 14 and 5 belong to the same group, whereas 13 and 3 belong to different groups.
# Return the number of groups that have the largest size, i.e. the maximum number of elements.

# Example 1:

# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], 
# [2,11], 
# [3,12], 
# [4,13], 
# [5], 
# [6], 
# [7], 
# [8], 
# [9].
# There are 4 groups with largest size.
n = 13
# --- My solution
class Solution:
    def countLargestGroup(self, n):
        groups = {}

        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            groups[digit_sum] = groups.get(digit_sum, 0) + 1

        max_size = max(groups.values())
        return sum(1 for size in groups.values() if size == max_size)       
# --- Test
sol = Solution()
print(sol.countLargestGroup(n))