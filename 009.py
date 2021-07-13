class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x = str(x)
        ls = 0
        rs = len(x)-1
        while (ls<=rs):
            if x[ls] == x[rs]:
                ls = ls+1
                rs = rs-1
            else:
                return False

        return True

sol = Solution()
print(len(str(0)))
print(sol.isPalindrome(0))