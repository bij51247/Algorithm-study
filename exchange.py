a = 10
b = 5
print('a:',a)
print('b:',b)

tmp = a
a = b
b = tmp
print('a:',a)
print('b:',b)

a,b = b,a
print('a:',a)
print('b:',b)