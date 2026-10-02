# https://leetcode.com/problems/add-binary/description/
# Given two binary strings a and b, return their sum as a binary string.
# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
a = "11"
b = "1"
# --- My solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = max(len(a), len(b)) + 1
        a = a.zfill(l)
        b = b.zfill(l)
        ans = []
        c = 0
        for i in range(l -1,-1,-1):
            x = int(a[i]) + int(b[i]) + c
            ans.append(x % 2)
            c = x // 2
        ans.reverse()
        res = "".join(str(d) for d in ans)

        return res.lstrip("0") or "0"
    # Yeah there is a easier version using bin
# --- Test
sol = Solution()
print(sol.addBinary(a,b))