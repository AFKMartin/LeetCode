# https://leetcode.com/problems/customers-who-never-order/description/
# Write a solution to find all customers who never order anything.
# Return the result table in any order.
# The result format is in the following example.
# data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
# customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
# data = [[1, 3], [2, 1]]
# orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})
# --- My solution
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    result = merged[merged['customerId'].isna()][['name']]
    return result
# --- Test
print(find_customers(customers))