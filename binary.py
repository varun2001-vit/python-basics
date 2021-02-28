def bs(a,ele):
    first=0
    last=len(a)-1
    found=False
    while first<=last and not found:
        mid=(first+last)//2
        if(a[mid]==ele):
            found=True
            pos=mid
        else:
            if ele<a[mid]:
                last=mid -1
            else:
                first=mid+1
    return  found,pos
a=[1,2,4,6,7,8,9]
print(bs(a,6))

