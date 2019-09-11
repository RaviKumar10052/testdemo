t=input().split(" ")
n=int(t[0])
x=int(t[1])
def hp(v):
    res = 0
    for i in range(v, 0, -1):
        if ((i & (i - 1)) == 0):
            res = i
            break
    return res
p=hp(x)
l=[1]*n
sum=0
i=1
while(sum<x):
    l[n-i]=p
    sum=sum+p
    p=p//2
    i=i+1
d=sum-x
l[n-i+1]=l[n-i+1]-d
if((n-i+1)%2==1):
    l[n-i+1]=l[n-i+1]+1
for j in range(n):
    print(l[j],end=" ")
