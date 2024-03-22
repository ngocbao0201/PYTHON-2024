def sum(n) :
    s = int(0)
    for i in range(1,len(n),2):
        s += int(n[i])
    return s

def mul(n) :
    m = int(1)
    for i in range(0,len(n),2):
        if int(n[i]) != 0 :
            m = m * int(n[i])
    return m

for t in range(int(input())) :
    n = input()
    print(mul(n), sum(n))