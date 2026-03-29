class Solution(object):
    def intToRoman(self, num):
        values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        syms=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res=""
        n=len(values)
        for i in range(n):
            while num>=values[i]:
                res=res+syms[i]
                num=num-values[i]
        return res
#o(n)