import math

class phan_so :
    def __init__(self,x,y) :
        u = math.gcd(x,y)
        self.x = int(x/u)
        self.y = int(y/u)

arr = input().split()
a = phan_so(int(arr[0]),int(arr[1]))
print(str(a.x) + '/' + str(a.y))
        