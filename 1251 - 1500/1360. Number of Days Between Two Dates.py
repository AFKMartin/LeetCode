# https://leetcode.com/problems/number-of-days-between-two-dates/description
# Write a program to count the number of days between two dates.
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

# Example 1:

# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
date1 = "2020-01-15" 
date2 = "2019-12-31"
# --- My solution
class Solution:
    def daysBetweenDates(self, date1, date2):
        def to_days(date):
            y, m, d = map(int, date.split("-"))
            months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
            leaps = (y - 1) // 4 - (y - 1) // 100 + (y - 1) // 400
            is_leap = y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
            return y * 365 + leaps + months[m - 1] + d + (1 if m > 2 and is_leap else 0)
        
        return abs(to_days(date1) - to_days(date2))
        
# --- Test
sol = Solution()
print(sol.daysBetweenDates(date1,date2))