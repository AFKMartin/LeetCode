# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/
# You are given two positive integers n and k. There are n children numbered from 0 to n - 1 standing in a queue in order from left to right.
# Initially, child 0 holds a ball and the direction of passing the ball is towards the right direction. After each second, the child holding the ball passes it to the child next to them. Once the ball reaches either end of the line, i.e. child 0 or child n - 1, the direction of passing is reversed.
# Return the number of the child who receives the ball after k seconds.

# Example 1:
# Input: n = 3, k = 5
# Output: 1
n = 3
k = 5
# --- My solution
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        c = 2 * (n - 1)
        t = k % c
        if t < n:
              return t + 1
        else:
              return 2*n - 1 - t
# --- Test
sol = Solution()
print(sol.numberOfChild(n, k))

