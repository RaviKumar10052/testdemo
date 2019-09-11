n = int(input())
l1 = []
l2 = []
a = 0
b = 1
for i in range(n):
    x = input().split(" ")
    t=int(x[0])
    l1.append(t)
    l2.append(x[1])

out = []
for i in range(20):
    out.append("|                    |")

for i in range(n):
    if (l2[i] == "E"):
        out[a] = out[a][:b] + "-" * l1[i] + out[a][b + l1[i]:]
        b = b + l1[i]
    if (l2[i] == "W"):
        out[a] = out[a][:b - l1[i]] + "-" * l1[i] + out[a][b:]
        b = b - l1[i]
    if (l2[i] == "N"):
        for j in range(l1[i]):
            out[a] = out[a][:b] + "|" + out[a][b + 1:]
            a = a - 1
    if (l2[i] == "S"):
        for j in range(l1[i]):
            out[a] = out[a][:b] + "|" + out[a][b + 1:]
            a = a + 1
    if (l2[i] == "NE"):
        for j in range(l1[i]):
            out[a] = out[a][:b] + "/" + out[a][b + 1:]
            b = b + 1
            a = a - 1
    if (l2[i] == "NW"):
        for j in range(l1[i]):
            out[a] = out[a][:b] + "\\" + out[a][b + 1:]
            b = b - 1
            a = a - 1
    if (l2[i] == "SE"):
        for j in range(l1[i]):
            out[a] = out[a][:b] + "\\" + out[a][b + 1:]
            b = b + 1
            a = a + 1
    if (l2[i] == "SW"):
        for j in range(l1[i]):
            out[a] = out[a][:b] + "/" + out[a][b + 1:]
            b = b - 1
            a = a + 1

for i in range(10):
    print(out[i])