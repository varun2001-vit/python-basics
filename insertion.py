def insertion(alist):
    for index in range(1,len(alist)):
        value=alist[index]
        i=index-1
        while(i>=0):
            if(alist[i+1]<alist[i]):
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
                i=i-1
            else:
                break
a=[1,4,2,3,6,5,7,4]
insertion(a)
print(a)