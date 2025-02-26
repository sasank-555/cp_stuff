########################################################################################################################
# -----------------------------------------------AUTHOR: shank_555-----------------------------------------------------#
########################################################################################################################
import sys
from collections import Counter, defaultdict, deque
import math

def input():
    return sys.stdin.readline().rstrip("\r\n")

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    orig = n 

    mx = orig + 1
    SPF = [i for i in range(mx)]
    for i in range(2, int(mx**0.5) + 1):
        if SPF[i] == i:
            for j in range(i * i, mx, i):
                if SPF[j] == j:
                    SPF[j] = i

    st = set()
    temp = n
    while temp != 1:
        pf = SPF[temp]
        st.add(pf)
        temp //= pf

    # Compute Euler's Totient function: φ(n) = n * Π(p-1)/p for each prime factor p
    ans = orig
    for p in st:
        ans *= (p - 1)
    for p in st:
        ans //= p

    print(ans)

if __name__ == '__main__':
    solve()
