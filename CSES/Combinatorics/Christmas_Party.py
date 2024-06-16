import functools

@functools.lru_cache(None)
def d(i):
    if i == 1 or i == 0:
        return 1-i
    return (i - 1) * (d(i - 2) + d(i - 1))


n = int(input().strip())

print(d(n))
