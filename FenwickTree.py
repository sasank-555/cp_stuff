# hmm u can use class if u want
n = 200
tree = [0]*(n + 1) # one based index
# sum upto i
def sum(i):
    i+=1
    ret = 0
    while i > 0:
        ret+=tree[i]
        i-= (i & -i)
    return ret
def add(i,delta):
    i+=1
    while i<=n:
        tree[i]+=delta
        i+= (i & -i)
def range_add(l,r,delta):
    add(l,delta)
    add(r + 1,-delta)
def pointval(i):
    return sum(i)


