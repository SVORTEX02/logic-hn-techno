for i in range(9):
    for j in range(9):
        if i+j<= 4 or j-i>=4 or i-j >=4 or i+j>=12:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print('')    

n = 19
x = int(n/2)
for i in range(n):
    for j in range(n):
        if i+j <= x or j-i>=x or i-j >=x or i+j>=x*3:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print('')    

n = 9
x = int(n/2)
for i in range(n):
    for j in range(n):
        if i+j <= x or j-i>=x or i-j >=x or i+j>=x*3:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print('')   