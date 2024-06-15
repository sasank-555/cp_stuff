class segmentTree:
    def __init__(self,nums):
        self.n= len(nums)
        self.tree = [0]*(4*n)
        self.build(nums,0,0,self.n -1)

  
    def build(self,nums,index , low , high):
        if(low==high) :
            self.tree[index] = nums[low]
        else:
            mid = (low+high)//2
            self.build(nums,2*index+1,low,mid)
            self.build(nums,2*index+2,mid+1,high)
            self.tree[index] = min(self.tree[2*index+1], self.tree[2*index+2])

    
    
    def rangeQuery_(self,index,low,high,left,right):
        if low>=left and high<=right:
            return self.tree[index]
        elif (low > right or high < left) :
            return float('inf')
        else:
            mid = (low+high)//2
            l = self.rangeQuery_(2*index+1,low,mid,left,right)
            r = self.rangeQuery_(2*index+2,mid+1,high,left,right)
            return min(l,r)
        
    
    def rangeQuery(self,left,right):
        return self.rangeQuery_(0,0,self.n-1,left,right) 


    def update_(self,i,val,index,low,high):
        if low==high:
            self.tree[index] = val
            return
        mid = (low+high)//2
        if i > mid:
            self.update_(i,val,2*index+2,mid+1,high)
        else:
            self.update_(i,val,2*index+1,low,mid)
        self.tree[index] = min(self.tree[2*index+1], self.tree[2*index+2])
            
    def update(self,i,val):
        return self.update_(i,val,0,0,self.n-1)
            
        