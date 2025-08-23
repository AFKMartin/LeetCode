# https://leetcode.com/problems/day-of-the-year/description
# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

# Example 1:

# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
date = "2019-01-09"
# --- My solution
class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        day = int(date[8:10])
        month = int(date[5:7]) - 1
        year = int(date[0:4])
        leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
        if leap and month > 1:
            return days[month] + day + 1
        else:
            return days[month] + day


# --- Test
sol = Solution()
print(sol.dayOfYear(date))