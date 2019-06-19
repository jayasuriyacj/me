from itertools import combinations
s1,a1=map(int,input().split())
b1=len(str(s1))
c1=list(combinations(str(s1),b1-a1))
c1=(sorted(c1))
d1="".join(c1[0])
print(d1)
