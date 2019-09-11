n= int(input())
l=["0"*(2*n-1)]*(2*n-1)
l[0]=l[0][:0]+str(n)*(2*n-1)
for i in range(2*n-1):
    l[i]=str(n)+l[i][1:]
    #print(l[i])
#print()
for i in range(1,n):
    for j in range(1,2*n-1):
        if(i==j):
            l[i]=l[i-1][:j]+str(int(l[i-1][j])-1)*(2*n-1-2*i)+l[i-1][j+(2*n-1-2*i):]
j=0
for i in range (2*n-2,n-1,-1):
    l[i]=l[i][:0]+l[j]
    j=j+1

for i in range(2*n-1):
    print(l[i])




