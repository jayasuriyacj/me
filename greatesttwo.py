inp1=list(map(int,input().split()))
inp2=inp1[0]
inp3=inp1[1]
def gcd(inp2,inp3):
    if inp3==0:
        print(inp2)
    else:
        gcd(inp2,inp2%inp3)
gcd(inp2,inp3)
