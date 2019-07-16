inp1=int(input())
inp2=list(map(int,input().split()))[:inp1]
for i in range(0,inp1):
  print(inp2[i],i)
