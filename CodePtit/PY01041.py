def m_a_x(n):
    m = int(n[0])
    for i in range(1,len(n)) :
        if int(n[i]) > m :
            m = int(n[i])
    return m

def check(n) :
    if len(n) < 3 :
        return False
    else :
        m = m_a_x(n)
        j = 0
        for i in range(0,len(n)) :
           if int(n[i]) == m :
               j = i
               break
        for i in range(0,j) :
            if int(n[i]) >= int(n[i+1]) :
                return False
        for i in range(j,len(n)-1) :
            if int(n[i]) <= int(n[i+1]) :
                return False
    return True

for t in range(int(input())) :
    n = input()
    if check(n) :
        print("YES")
    else :
        print("NO")