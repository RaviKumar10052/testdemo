N= int(input())
def gcd(a, b):
    if (a == 0 or b == 0): return 0
    if (a == b): return a

    if (a > b):
        return gcd(a - b, b)

    return gcd(a, b - a)

for i in range (N):
    for j in range(i+1,N):
        if(gcd(i,j)==1):
            print(i,j)
