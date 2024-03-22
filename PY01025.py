s = str(input())
x = s[::-1]
res = ''
for i in range(0,len(x)) :
    if i % 3 == 0 and i != 0 :
        res = res + ',' + x[i]
    else :
        res = res + x[i]
print(res[::-1])
