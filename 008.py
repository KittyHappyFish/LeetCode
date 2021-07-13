import re
class Solution:
    def myAtoi(self, s: str) -> int:
        max_s = 2**31-1
        min_s = -2**31
        s = s.lstrip()
        num = int(*re.findall('^[\+\-]?\d+',s))
        return max(min(num,max_s),min_s)

sol = Solution()
print(sol.myAtoi('     +52435123124   asdfsdf'))