n,k = map(int,input().split())
grid = []
for _ in range(n):
    s = list(map(lambda x : ord(x) - ord('A'),list(input())))
    grid.append(s)
def cal(nums):
    ans = 0
    N  = len(nums)
    nxt = [N]*len(nums)
    st = []
    for i in range(N-1,-1,-1):
        while st and nums[st[-1]]>=nums[i]:
            st.pop()
        if st:
            nxt[i] = st[-1]
        st.append(i)
    st = []
    prev  = [-1]*N
    for i in range(N):
        while st and nums[st[-1]] > nums[i]:
            st.pop()
        if st:
            prev[i] = st[-1]
        st.append(i)
    for i in range(len(nums)):
        r = nxt[i] - i
        l =  i - prev[i]
        ans+=nums[i]*l*r
    return ans
def numSubmat(mat,k):
    N,M = len(mat) , len(mat[0])
    for i in range(N):
        for j in range(M):
            mat[i][j] = 1 if mat[i][j]==k else 0
            if mat[i][j] and i > 0:
                mat[i][j]+=mat[i-1][j]
    ans = 0
    for x in mat:
        ans+=cal(x)
    return ans
import copy
for i in range(k):
    print(numSubmat(copy.deepcopy(grid), i))
