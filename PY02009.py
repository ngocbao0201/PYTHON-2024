for t in range(int(input())) :
    n = int(input())
    d = {}
    for i in range(0,n):
        m = int(input())
        if m in d :
            d[m] = d[m] + 1
        else:
            d.setdefault(m,int(1))
    max_value = max(d.values())
    l = []
    for i in d.keys() :
        if d[i] == max_value:
            l.append(i)
    l.sort()
    print(l[0])
    