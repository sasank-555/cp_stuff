from sortedcontainers import SortedList
# [1,2] [2,3] intersects here
class IntervalContainerBasic:
    def __init__(self):
        self.sl = SortedList()
    def add(self,l,r):
        if l > r:
            raise ValueError("left should be lesser than right")
        if self.intersects(l,r):
            return False
        self.sl.add([l,r])
        return True
    def intersects(self,l,r):
        j = self.sl.bisect_left([l,r])
        if j!=len(self.sl) and self.sl[j][0]<=r:
            return True
        j-=1
        if j>=0 and self.sl[j][1]>=l:
            return True
        return False
    def remove(self,l,r):
        self.sl.remove([l,r])
class IntervalContainerWithMerging:
    def __init__(self):
        self.sl = SortedList()
    
# inv = IntervalContainerBasic()
# print(inv.add(2,3))
# print(inv.add(9,8))
# print(inv.add(1,10))