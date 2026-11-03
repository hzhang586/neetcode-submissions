class Solution:
    def myPow(self, x: float, n: int) -> float:

        def f(x,n):
            if n == 0:
                return 1
            
            half = f(x,n//2)
            if n % 2 == 0:
                return half*half
            else:
                return x * half*half  

        return f(x,n) if n >= 0 else 1/f(x,-n)