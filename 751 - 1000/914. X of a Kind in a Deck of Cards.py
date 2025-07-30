# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
# You are given an integer array deck where deck[i] represents the number written on the ith card.
# Partition the cards into one or more groups such that:
# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.

# Example 1:

# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
deck = [1,1,1,2,2,2,2,2,3,3,3,3,3]
# --- My solution
class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        c = {}
        for card in deck:
            if card in c:
                c[card] +=1
            else:
                c[card] = 1
        c = list(c.values())

        def gcd(a,b):
            while b:
                a , b = b ,a % b
            return a

        size = c[0]
        for num in c[1:]:
            size = gcd(size, num)

        return size > 1
# If using math library it gets way simplier, I think.
# --- Test
sol = Solution()
print(sol.hasGroupsSizeX(deck))