fibo = [1,1]

for i in range(2,93):
    fibo.append(fibo[i-1] + fibo[i-2])
for t in range(int(input())) :
    a,b = (int(i) for i in input().split())
    for j in range(a-1,b) :
        print(fibo[j], end = ' ')
    print()