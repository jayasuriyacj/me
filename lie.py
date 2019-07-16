inp1,inp2=list(map(int,input().split()))
inp3,inp4=list(map(int,input().split()))
inp5,inp6=list(map(int,input().split()))
if inp1==inp2 or inp3==inp4 or inp5==inp6 or inp1==inp3==inp6 or inp2==inp4==inp5:
    print('yes')
else:
    print('no')
