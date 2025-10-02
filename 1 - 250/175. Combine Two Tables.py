# https://leetcode.com/problems/combine-two-tables/
# Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.
# Return the result table in any order.
# The result format is in the following example.
# --- My solution 
import pandas as pd

data = [[1, 'Wang', 'Allen'], [2, 'Alice', 'Bob']]

person = pd.DataFrame(data, columns=['personId', 'firstName', 'lastName']).astype({'personId':'Int64', 'firstName':'object', 'lastName':'object'})

data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]

address = pd.DataFrame(data, columns=['addressId', 'personId', 'city', 'state']).astype({'addressId':'Int64', 'personId':'Int64', 'city':'object', 'state':'object'})
# --- My solution
def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # merge allows you to merge two tables
    # on="personId" tells pandas to match rows from both DataFrames using the personId column (because is in both tables is the nexus)
    # how="left" tells pandas to keep all rows from person, even if they don’t have a matching address (fill NaN if missing wich is neat).
    res = pd.merge(person, address, on="personId", how="left") 
    # then you simply return the values you are asked for.
    return res[["firstName", "lastName", "city", "state"]]
# --- Test
print(combine_two_tables(person, address))
