def sortbubble(a):
    passnum=len(a)-1
    while(passnum>0):
        for i in range(passnum):
            if(a[i]>a[i+1]):
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
                print("after swap",a)
        passnum=passnum-1


def insert(list, n):
    # Searching for the position
    for i in range(len(list)):
        if list[i] > n:
            index = i
            break

    # Inserting n in the list
    list = list[:i] + [n] + list[i:]
    return list
a=[1,4,2,6,3]
sortbubble(a)
v=6
b=insert(a,v)
print(b)


