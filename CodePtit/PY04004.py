import math

class phan_so :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
    def rut_gon(self) :
        u = math.gcd(self.x,self.y)
        self.x = int(self.x/u)
        self.y = int(self.y/u)
    def add(self,i) :
        a = self.x * i.y + self.y * i.x
        b = self.y * i.y
        self.x = a
        self.y = b
    def output(self) :
        print(str(self.x) + '/' + str(self.y))
    

arr = input().split()
a = phan_so(int(arr[0]),int(arr[1]))
b = phan_so(int(arr[2]),int(arr[3]))
a.add(b)
a.rut_gon()
a.output()

    
        