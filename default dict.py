from collections import defaultdict
d=defaultdict(int)
a=[1,2,3,4,2,4,2,1,2]
for i in a:
    d[i]+=1
print(d)
