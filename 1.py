
a=input('Введите семизначное число')
b=0
c=0
for i in a:
    if a(int) % 2 == 0:
        b+=1
    else:
        c+=1
    print("Четных:",b, "Нечетных:",c)
sum=0
pr=1
if b>c:
    for i in a:
        sum +=i
    print("Сумма: ",sum)
else:
    pr=a[0]*a[2]*a[5]
    print("Произведение:",pr)


