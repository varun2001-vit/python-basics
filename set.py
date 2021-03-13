a=int(input())
b=int(input())
c=[[int(input()) for x in range (a)] for y in range(b)]
for i in range(a):
    for j in range(b):
        print(c[i][j])
