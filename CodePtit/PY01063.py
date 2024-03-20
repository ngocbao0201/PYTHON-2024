for t in range(int(input())) :
    n = input()
    m = input()
    cnt = int(0)
    i = int(0)
    while i <= len(n) - len(m) :
        if n[i:i+len(m)] == m :
            cnt = cnt + 1
            i = i + len(m)
        else :
            i = i + 1
    print(cnt)