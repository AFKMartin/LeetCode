# https://leetcode.com/problems/employees-earning-more-than-their-managers/
# Write a solution to find the employees who earn more than their managers.
# Return the result table in any order.
# The result format is in the following example.
import pandas as pd
data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]

employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})
# --- My solution
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee
    merge = df.merge(df, left_on="managerId", right_on="id", suffixes=("_emp", "_man"))
    merge = merge[merge["salary_emp"] > merge["salary_man"]]
    return merge[["name_emp"]].rename(columns={"name_emp": "Employee"})
# --- Test
print(find_employees(employee))