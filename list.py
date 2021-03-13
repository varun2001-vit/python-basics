list=[10,20,30,10,40,50,60,]
for i in range(9):
    sum=sum+list[i]
avg=sum/10
print('avg =',avg)
median=(list[4]+list[5])/2
print('median',median)
#standard devaition
for i in range(9):
    list[i]=list[i]-avg
print('stanadard devaiton =',list)
