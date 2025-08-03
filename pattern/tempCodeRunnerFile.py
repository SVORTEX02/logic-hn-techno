for i in range(9):
    for j in range(9):
        if i+j <= 4 or j-i>=4 or i-j >=4 or i+j>=12:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print('')    
