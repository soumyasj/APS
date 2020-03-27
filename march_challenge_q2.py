# cook your dish here
from sys import stdin,stdout
T=int(input())
for i in range(T):
    x,y=map(int,input().rstrip().split())
    a=list(map(int,input().rstrip().split()))
    
    odd=0
    for k in a:
        if((bin(k).count('1'))%2!=0):
            odd+=1
    for k in range(y):
        b=int(stdin.readline())
        if((bin(b).count('1'))%2==0):
            print(x-odd,odd)
        else:
            print(odd,x-odd)
    
