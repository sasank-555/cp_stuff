MAX = 100001
v = [False] * MAX
sp = [0] * MAX
for i in range(2, MAX, 2):
    sp[i] = 2
for i in range(3, MAX, 2):
    if not v[i]:
        sp[i] = i
        j = i
        while j * i < MAX:
            if not v[j * i]:
                v[j * i] = True
                sp[j * i] = i
            j += 2   
def getp(x):
    res = set()
    while x > 1:
        res.add(sp[x])
        x //= sp[x]
    return list(res)