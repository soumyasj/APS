T=int(input())
for i in range(T):
    x,y=map(int,input().strip().split())
    a=list(map(int,input().rstrip().split()))
    b=list(map(int,input().rstrip().split()))
    dict1=dict()
    s=list(set(a))
    for j in s:
        dict1[j]=0
    for j in range(len(a)):
        dict1[a[j]]=dict1[a[j]]+b[j]
    print(min(dict1.values()))
    
