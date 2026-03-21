# https://leetcode.com/problems/calculate-delayed-arrival-time/description
# You are given a positive integer arrivalTime denoting the arrival time of a train in hours, and another positive integer delayedTime denoting the amount of delay in hours.
# Return the time when the train will arrive at the station.
# Note that the time in this problem is in 24-hours format.

# Example 1:

# Input: arrivalTime = 15, delayedTime = 5 
# Output: 20 
# Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will reach at 15+5 = 20 (20:00 hours).
arrivalTime = 13
delayedTime = 11
# --- My solution
class Solution:
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        return (arrivalTime + delayedTime) % 24
# --- Test      
sol = Solution()
print(sol.findDelayedArrivalTime(arrivalTime, delayedTime))