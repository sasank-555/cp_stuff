import sys
input = sys.stdin.readline

def main():
    n, m, q = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x)-1, input().split())
        adj[u].append(v)
        adj[v].append(u)

    INF = 1 << 60
    dis = [[INF] * (2 * n) for _ in range(n)]

    for src in range(n):
        d = dis[src]
        d[src*2] = 0
        stack = [src*2]
        while stack:
            nxt = []
            for u in stack:
                i = u // 2
                for v in adj[i]:
                    dj = d[u] + 1
                    idx = v * 2 + (dj % 2)
                    if dj < d[idx]:
                        d[idx] = dj
                        nxt.append(idx)
            stack = nxt

    for _ in range(q):
        a, b, x = map(lambda x: int(x)-1, input().split())
        x += 1
        e = dis[a][b*2]
        o = dis[a][b*2+1]
        ok = (x >= e and (x - e) % 2 == 0) or (x >= o and (x - o) % 2 == 0)
        print("YES" if ok else "NO")

main()
