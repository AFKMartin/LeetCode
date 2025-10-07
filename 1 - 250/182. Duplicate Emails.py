# https://leetcode.com/problems/duplicate-emails/description/
import pandas as pd
data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})
# Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.
# Return the result table in any order.
# The result format is in the following example.

# Example 1:

# Input: 
# Person table:
# +----+---------+
# | id | email   |
# +----+---------+
# | 1  | a@b.com |
# | 2  | c@d.com |
# | 3  | a@b.com |
# +----+---------+
# -- My solution
def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    res = (
        person.groupby("email")
        .size()
        .reset_index(name="count")
        .query("count > 1")[["email"]]
    )
    return res
# -- Test
print(duplicate_emails(person))