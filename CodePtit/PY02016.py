for t in range(int(input())) :
    n = int(input())
    l = list(map(int,input().split()))
    d = {}
    for i in l :
        if i in d.keys() :
            d[i] = d[i] + 1
        else:
            d.setdefault(i,1)
    m = max(d.values())
    if m > n/2 :
        ls = []
        for i in d.keys() :
            if d[i] == m :
                ls.append(i)
        ls.sort()
        print(ls[0])
    else :
        print("NO")
                
    
            
            
    