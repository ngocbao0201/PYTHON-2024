def uscln(a,b) :
    if b == 0 :
        return a
    return uscln(b,a%b)

for t in range(0,int(input())) :
    a = input()
    b = a[::-1]
    if uscln(int(a),int(b)) == 1 :
        print("YES")
    else :
        print("NO")
