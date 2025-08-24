# https://leetcode.com/problems/day-of-the-week/description
# Given a date, return the corresponding day of the week for that date.
# The input is given as three integers representing the day, month and year respectively.
# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
# The given dates are valid dates between the years 1971 and 2100.
# Example 1:
# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
day = 1
month = 1
year = 1971
# --- My solution
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # 01/01/1971 = friday
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def is_leap(y):
            return (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0)
        
        days = 0
        for y in range(1971, year):
            days += 366 if is_leap(y) else 365
        
        for m in range(month - 1):
            days += days_per_month[m]
            if m == 1 and is_leap(year):
                days += 1
        
        days += day - 1

        return week[(days + 5) % 7]
# --- Test
sol = Solution()
print(sol.dayOfTheWeek(day, month, year))