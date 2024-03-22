def check(n) :
    for i in range(1,len(n),2) :
        if int(n[i]) != 0 :
            return False
    return True

def sum(n):
    s = int(0)
    for i in range(0,len(n),2) :
        s += int(n[i])
    return s

def tich(n):
    m = int(1)
    for i in range(1,len(n),2) :
        if int(n[i]) != 0 :
            m = m * int(n[i])
    return m

for t in range(int(input())) :
    n = input()
    if check(n) :
        print(sum(n), '0')
    else :
        print(sum(n), tich(n))