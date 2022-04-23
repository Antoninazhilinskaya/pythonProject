a=input('Введите строку:')
gl=0
sgl=0
for i in a:
    if i in "aeyoi":
        gl+=1
    else:
        sgl+=1
print("Гласных",gl,"Согласных",sgl)
    
