def var(n):
   if n>0:
     res=n+var(n-1)
     print(res)
   else:
     res=0
   return res
var(6)
