import math

for t in range(int(input())) :
    a = int(input())
    res = '1'
    for i in range(2,int(math.sqrt(a)+1)) :
        cnt = 0
        while a % i == 0 :
            a = int(a/i)
            cnt = cnt + 1
        if cnt > 0 :
            res += ' * ' + str(i) + '^' + str(cnt)
        if a == 1 :
            break
    if a > 1 :
        res += ' * ' + str(a) + '^1'
    print(res)