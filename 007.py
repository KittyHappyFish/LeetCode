class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        flg = -1 if x<0 else 1
        x = abs(x)
        # -2147483648 < x < 2147483647
        while (x!=0):
            if (res>214748364): return 0
            res = res*10
            res = res + x % 10
            x //= 10
            
        return res * flg


s = Solution()
print(s.reverse(-2147483412))