import random
mod = random.getrandbits(64)
p = random.randint(150,2*150)

class straightHash:
    def __init__(self,s):
        self.s = s
        self.pp = [1]
        self.h = [0]
        for c in s:
            self.h.append((self.h[-1]*p + ord(c))%mod)
            self.pp.append((self.pp[-1]*p)%mod)
    def query(self,l,r):
        return (self.h[r + 1] - self.h[l]*self.pp[r - l + 1])%mod 
class ReverseHash:
    def __init__(self,s):
        self.s = s[::-1]
        self.rh = [0]
        self.rpp = [1]
        for x in self.s:
            self.rh.append((self.rh[-1]*p + ord(x))%mod)
            self.rpp.append((self.rpp[-1] *p)%mod)
    def query(self,l,r):
        N  = len(self.s)
        r = N - l  - 1
        l = N - r - 1
        return (self.rh[r + 1] - self.rh[l]*self.rpp[r - l + 1])%mod
        

