n=15
a=[3,5,10]

res=[0 for i in range(n+1)]

res[0]=1

for i in a:
    for j in range(len(res)):
        if(j>0):
            if(res[j-i]>=1):
                res[j]=res[j]+1
print(res)

