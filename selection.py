def sortbubble(a):
    passlen=len(a)-1
    while(passlen>0):
        for i in range(passlen):
            if(a[i]>a[i+1]):
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
                print("after swap",a)
        passlen=passlen-1
b=[1,4,2,6,3]
sortbubble(b)
print(b)