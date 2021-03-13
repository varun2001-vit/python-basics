def selection(alist):
    for i in range(len(alist)-1):
        min=i
        for j in range(i+1,len(alist)):
            if(alist[j]<alist[min]):
                temp=alist[min]
                alist[min]=alist[j]
                alist[j]=temp
                j=j+1
a=[1,3,2,5,4,9,7,8]
selection(a)
print(a)