a=[4,6,'py','tell',78]
b=[44,'hello',56,'exept',3]
c=a+b
print(c)

c.insert(3,6)
print(c)

del c[2]
del c[3]
c.remove('hello')
c.remove('exept')
print(c)

count=len(c)
print(count)

