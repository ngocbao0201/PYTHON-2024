n = int(input())
s = input().split()
list_diem = []
for i in s :
    list_diem.append(float(i))
list_diem.sort()
max = list_diem[-1]
min = list_diem[0]
list_diem_TB = []
for i in list_diem :
    if i != min and i != max :
        list_diem_TB.append(i)
sum = 0 
for i in list_diem_TB :
    sum = sum + float(i/len(list_diem_TB))
print("{:.2f}".format(sum))



    
