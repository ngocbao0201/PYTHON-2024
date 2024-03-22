def chan(n):
    return n/2

def le(n):
    return n*3+1

while(True):
    n = int(input())
    if n == 0 : break
    cnt = int(1)
    while n>1 :
        if n % 2 == 0:
            n = chan(n)
            cnt += 1
        else :
            n = le(n)
            cnt +=1
    print(cnt)