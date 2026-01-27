class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend>2**31 ):
            return 2**31 -1
        else if(dividend<-2**31):
            return -2**31
        else if(dividend==-2147483648 and divisor ==-1):
            return    2**31 -1
        x = dividend/divisor
        y = str(x)
        a= y.split(".")
        if(dividend>=-2**31 and dividend<2**31):
            return int(a[0])
