def lN(array):
    extval=[]
    ans =""
    l = len(str(max(array))) + 1
    for i in array:
        temp = str(i) * l
        extval.append((temp[:l:], i))
    extval.sort(reverse=True)
    for i in extval:
        ans += str(i[1])
    return ans

print(lN(array))
