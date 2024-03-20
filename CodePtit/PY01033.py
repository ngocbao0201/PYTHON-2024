import math

def check(a,b) :
    if math.gcd(int(a),int(b)) == 1 :
        return True
    return False

l,r = (int(i) for i in input().split())
r = r + 1
for i in range(l,r) :
    for j in range(i+1,r) :
        for k in range(j+1,r) :
            if check(i,j) and check(i,k) and check(j,k) :
                print( "(" , end = '')
                print( i , end=', ')
                print( j , end=', ')
                print( k , end=')\n')