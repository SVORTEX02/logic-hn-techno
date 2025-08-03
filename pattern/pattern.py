n=11
p=n//2
for i in range(n):
    for j in range(n-1):
        if (j==0) or (i-j==0 and (i<=p)) or (i+j==n-1 and (i>=p)) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# n=5
# for i in range(0,n+1):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()