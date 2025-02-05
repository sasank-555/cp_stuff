def extend_gcd(a, b):
    sub = dict()
    stack = [(a, b, 0)]
    while stack:
        a, b, s = stack.pop()
        if a == 0:
            sub[(a, b)] = (b, 0, 1) if b >= 0 else (-b, 0, -1)
            continue
        if s == 0:
            stack.append((a, b, 1))
            stack.append((b % a, a, 0))
        else:
            gcd, x, y = sub[(b % a, a)]
            sub[(a, b)] = (gcd, y - (b // a) * x, x) if gcd >= 0 else (-gcd, -y + (b // a) * x, -x)
            assert gcd == a * (y - (b // a) * x) + b * x
    return sub[(a, b)]

def find_any(a, b, c):
    gcd, x, y = extend_gcd(a, b)
    assert a * x + b * y == gcd
    if c % gcd:
        return []
    x0 = x * (c // gcd)
    y0 = y * (c // gcd)
    return [x0, y0,gcd]

def shift_solution(x, y, a, b, cnt):
    x += cnt * b
    y -= cnt * a
    return x, y

def find_in_range(a, b, c, minx, maxx, miny, maxy):
    t = find_any(a, b, c)
    if len(t) == 0:
        return 0
    x, y, g = t
    a //= g
    b //= g
    sign_a = 1 if a > 0 else -1
    sign_b = 1 if b > 0 else -1

    # Adjust x to the minimum x range
    x, y = shift_solution(x, y, a, b, (minx - x) // b)
    if x < minx:
        x, y = shift_solution(x, y, a, b, sign_b)
    if x > maxx:
        return 0
    lx1 = x

    # Adjust x to the maximum x range
    x, y = shift_solution(x, y, a, b, (maxx - x) // b)
    if x > maxx:
        x, y = shift_solution(x, y, a, b, -sign_b)
    rx1 = x

    # Adjust y to the minimum y range
    x, y = shift_solution(x, y, a, b, -(miny - y) // a)
    if y < miny:
        x, y = shift_solution(x, y, a, b, -sign_a)
    if y > maxy:
        return 0
    lx2 = x

    # Adjust y to the maximum y range
    x, y = shift_solution(x, y, a, b, -(maxy - y) // a)
    if y > maxy:
        x, y = shift_solution(x, y, a, b, sign_a)
    rx2 = x

    # Ensure lx2 and rx2 are in proper order
    if lx2 > rx2:
        lx2, rx2 = rx2, lx2

    # Compute the overlapping x range
    lx = max(lx1, lx2)
    rx = min(rx1, rx2)
    if lx > rx:
        return 0
    return (rx - lx) // abs(b) + 1
