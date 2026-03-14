# https://leetcode.com/problems/count-days-spent-together/description

# Alice and Bob are traveling to Rome for separate business meetings.
# You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.
# Return the total number of days that Alice and Bob are in Rome together.
# You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

# Example 1:

# Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
# Output: 3
# Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
arriveAlice = "10-01"
leaveAlice = "10-31"
arriveBob = "11-01"
leaveBob = "12-31"
# --- My solution
from datetime import datetime

class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        fmt = "%m-%d"

        y = max(arriveAlice, arriveBob)
        x = min(leaveAlice, leaveBob)
        
        if y > x:
            return 0

        d1 = datetime.strptime(y, fmt)
        d2 = datetime.strptime(x, fmt)

        return (d2 - d1).days + 1
    
# --- Test
sol = Solution()
print(sol.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))