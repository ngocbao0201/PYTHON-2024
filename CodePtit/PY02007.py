def devide(n) :
    return int(n) % 42

a = list(map(int,input().split()))
while len(a) < 10 :
    a = a + list(map(int,input().split()))
b = map(devide,a)
print(len(set(b)))
