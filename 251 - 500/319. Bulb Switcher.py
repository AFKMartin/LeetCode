# https://leetcode.com/problems/bulb-switcher/description
# There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.
# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
# Return the number of bulbs that are on after n rounds.

# Example 1:

# Input: n = 3
# Output: 1
# Explanation: At first, the three bulbs are [off, off, off].
# After the first round, the three bulbs are [on, on, on].
# After the second round, the three bulbs are [on, off, on].
# After the third round, the three bulbs are [on, off, off]. 
# So you should return 1 because there is only one bulb is on.
n = 100
# --- My solution
class Solution:
    def bulbSwitch(self, n: int) -> int:
        #if n == 0 or n == 1: # edge cases # actually you don't need this but this was my initial code so I'll let it be like this
            #return n
        #else:
            return int(n**0.5) # math trick for this you only need to do this
# --- Test
sol = Solution()
print(sol.bulbSwitch(n))