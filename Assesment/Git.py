a=list(int(input()))
target=int(input())
for i in range(len(a)):
    for j in range(i):
        if(a[i]+a[j]==target):
            print(i,j)