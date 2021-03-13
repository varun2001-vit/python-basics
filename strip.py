print('enter a')
a=input()
b=len(a)
if  b< 2:
    print()
else:
    c = a[:2] + a[b-2:b]
    print(c)

