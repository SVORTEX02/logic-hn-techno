#pattern 1
"""for i in range(1,6,1):
    for j in range(1,6,1):
        print(j,end=" ")
    print()"""
#out put
"""
1 2 3 4 5 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

#pattern-2
"""for i in range(1,6,1):
    for j in range(1,6,1):
        print(i,end=" ")
    print()"""
"""
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5"""           

"""count = 1
for count in range(1,21):
    print(count,end=' ')  
    count=count+1  
    if count % 5 == 1:  
        print()  
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15
16 17 18 19 20"""
"""k=1
for i in range(1,6):
    for j in range(1,6):
        print(k,end=" ")
        k=k+1
    print()
"""


"""for i in range(1,6,1):
    for j in range(1,6,1):
          print("*1",end="")
    print()

*1*1*1*1*1
*1*1*1*1*1
*1*1*1*1*1
*1*1*1*1*1
*1*1*1*1*1
    """

"""for i in range(1,5,1):
    if(i%2==1):
        print("1*1*1*")
    else:
        print("*1*1*1")
1*1*1*
*1*1*1
1*1*1*
*1*1*1"""
"""
k=1
for i in range(1,6):
    for j in range(1,6):
        print(k,end="")
        k=k+1
        if(k==10):
            k=1
    print()

12345
67891
23456
78912
34567"""

"""for i in range(1,6):
    print(end="*")
    for j in range(1,6,*2):
        print(j,end="*")
    print()"""
"""n=10
for i in range(1,n):
    for j in range(1,i+1):
            print(j,end=" ")
    print()
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9"""

"""n=10
for i in range(n):
    for j in range(1,n-i):
        print(j,end=" ")
    print()"""
"""
1 2 3 4 5 6 7 8 9      
1 2 3 4 5 6 7 8      
1 2 3 4 5 6 7       
1 2 3 4 5 6     
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1"""

"""k=5
for i in range(0,5):
    print("*"*(k-i),end="")
    for j in range(i+1):
        print("*",end="")
    print()"""



"""n = 5
p = 4
i = 1
x = 1
c = 1

while c <= p:
    print(i, end="")
    if x % n == 0:
        print()  # for new line
        x = 0
    if i == 9:
        i = c
        c += 1
    i += 1
    x += 1

12345
67892
34567
89345
67894
56789"""

"""x = 1
c = True

for i in range(1, 26):
    print(x, end=" ")
    
    if x == 9:
        c = False
    if x == 1:
        c = True
    
    if c:
        x += 1
    else:
        x -= 1
    
    if i % 5 == 0:
        print()  # Prints a new line after every 5th iteration

1 2 3 4 5 
6 7 8 9 8
7 6 5 4 3
2 1 2 3 4
5 6 7 8 9
"""


"""for j in range(1,6):
     for i in range(1,6):
         print(j,end='')
     print('')   
11111
22222
33333
44444
55555 """
  
"""for j in range(1,6):
     for i in range(1,6):
         print(i,end='')
     print('')  
12345
12345
12345
12345
12345"""
"""k = 1
for j in range(1,6):
    for i in range(1,6):
        print(k,end='')
        k+=1
    print('') 

12345
678910
1112131415
1617181920
2122232425"""

"""
k=1
for i in range(1,6):
    for j in range(1,6):
        print(k,end='')
        k+=1
        if k == 10:
            k = 1
    print('')

12345
67891
23456
78912
34567"""


