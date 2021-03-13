def insertion(alist):
    for i in range(1,len(alist)):
        current=alist[i]
        positon=i
        print(i,alist)
        while positon >0 and alist[positon-1]>current:
            alist[positon]=alist[positon-1]
            positon=positon-1
            alist[positon]=current
            print(i,alist,'in while')
alist=[1,5,4,6,7,2,3]
insertion(alist)
print(alist)