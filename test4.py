i1=int(input())
i2=input()
i3=input()
i4=input()
s=[]

for i in range (i1):
    s.append(i4[i])

def foo(str):
    n = len(str)
    opsize = pow(2, n)
    subs=[]
    for i in range(1,opsize+1):
        for j in range(n):
            if (j & (1 << j)):
                print(str[j])
                subs.append(str[j])
                print(subs)
    return subs

print(s)
res=foo(s)
l=[]
for x in res:
    if(x[0]==i2 and x[len(x)-1]==i3):
        l.append(x)


print(l)
print(len(l))