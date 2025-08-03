"""n = 5
x = n * 2 - 1
p = int(n/2)
for i in range(n):
    for j in range(x):
        if i+j == n-1 or j-i == n-1 or (i==p and j>=p and j<=p*3):
            print('*',end='')
        else:
            print(' ',end='')
    print('') 

    *    
   * *
  *****
 *     *
*       *"""


"""n=5
x=n*2-1
p=n//2

for i in range(0,n):
    for j in range(x):
        if((i==0 and j>=1 and j<=n-1)or j==0 or (i==1 and j==5) or (i==3 and j==5) or (i==4 and j>=1 and j<=n-1) or (i==p and j>=1 and j<=p*2 )):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

* * * * *
*         *
* * * * *
*         *
* * * * *"""
"""n=7
p=round(n//2)
for i in range(n):
    for j in range(n):
        if(j==0 or(j==n-1 and (i!=0 and i!=p and i!=n-1 ))) or ((i==0 or i==p or i==n-1)and(j>0 and j<n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 

* * * * * *   
*           *
*           *
* * * * * *
*           *
*           *
* * * * * *"""

"""n=7
for i in range(n):
    for j in range(n):
        if((j==0 and i!=0 and i!=n-1))or((i==0 or i==n-1) and (j!=0)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

 * * * * * * 
*
*
*
*
*
  * * * * * *"""

"""n=5
for i in range(n):
    for j in range(n):
        if(j==0 or(j==n-1 and (i!=0 and i!=n-1 ))) or ((i==0 or i==n-1)and(j>0 and j<n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

* * * *   
*       *
*       *
*       *
* * * *"""

"""n=5
p=n//2
for i in range(n):
    for j in range(n):
        if(j==0 or i==0 or i==n-1 or i==p):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

* * * * * 
*
* * * * *
*
* * * * *"""

"""n=5
p=n//2
for i in range(n):
    for j in range(n):
        if(j==0 or i==0 or i==p):
            print("*",end=" ")
        else:
            print(" ",end="")
    print()

* * * * * 
*
* * * * *
*
*"""

"""n=5
p=n//2
for i in range(n):
    for j in range(n):
        if(j==0 and (i>0 and i<n-1))or((i==0 or i==n-1)and(j!=0))or(j==n-1 and (i>=p and i<n-1)) or (i==p and(j>1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

  * * * * 
*
*   * * *
*       *
  * * * *"""

"""n=5
p=n//2
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1 or i==p):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
*       * 
*       *
* * * * *
*       *
*       *"""

"""n=5
p=n//2
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==p):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

* * * * * 
    *
    *
    *
* * * * *"""
"""n=5
p=n//2
for i in range(n):
    for j in range(n):
        if(i==0 or j==p)or(i==n-1 and(j>0 and j<=p)) or(j==0 and(i>=p and i<n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

* * * * * 
    *
*   *
*   *
  * *   """

"""n=5
p=n//2
for i in range(0,n):
    for j in range(0,n):
        if(j==0 or i+j==3 or i==j+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
*     *   
*   *
* *
*   *
*     *    """

"""n=5
p=n//2
for i in range(n):
    for j in range(n):
        if (j==0) or (i==n-1 and(j!=n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
*
*
*
*
* * * *

"""

"""n=5
x=n*2-1
p=n//2
for i in range(n):
    for j in range(x):
        if (j==0 or i==j or j==x-1 or i+j==x-1 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

*               * 
* *           * *
*   *       *   *
*     *   *     *
*       *       *  """
"""n=5
p=n//2
for i in range(n):
    for j in range(n):
        if (j==0) or (i-j==0 and (i<=p)) or j==n-1 or (i+j==n-1 and(i<=p)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

*       * 
* *   * *
*   *   *
*       *
*       *
"""

"""
n=5
p=n//2
for i in range(n):
    for j in range(n):
        if(j==0 or i==j or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

*       * 
* *     *
*   *   *
*     * *
*       *"""


"""n=7
p=n//2
for i in range(n):
    for j in range(n):
        if(j==0 and (i>0 and i<n-1)) or (i==0 and (j>0 and j<n-1)) or (j==n-1 and (i!=0 and i!=n-1)) or (i==n-1 and (j>0 and j<n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

  * * * * *   
*           *
*           *
*           *
*           *
*           *
  * * * * *
  """
"""
n=7
p=n//2
for i in range(n):
    for j in range(n):
        if(j==0) or(i==0 and(j!=n-1)) or(j==n-1 and (i!=0 and i<p)) or (i==p and(j>0 and j<n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
* * * * * *   
*           *
*           *
* * * * * *
*
*
*
"""
"""n=7
p=n//2
for i in range(n+1):
    for j in range(n):
        if(j==0 and (i>0 and i<n-1)) or (i==0 and (j>0 and j<n-1)) or (j==n-1 and (i!=0 and i!=n-1)) or (i==n-1 and (j>0 and j<n-1)) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

  * * * * *   
*           *
*           *
*           *
*           *
*           *
  * * * * *
            *
"""
"""n=7
p=n//2
for i in range(n+1):
    for j in range(n):
        if(j==0) or(i==0 and(j!=n-1)) or(j==n-1 and (i!=0 and i<p)) or (i==p and(j>0 and j<n-1)) or(i==j+2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
* * * * * *   
*           *
*           *
* * * * * *
*   *
*     *
*       *
*         *
"""
"""n=9
p=n//2
for i in range(n+1):
    for j in range(n):
        if (i==0 and(j>0 and j<n-1)) or (j==0 and(i>0 and i<p)) or (i==p and(j>0 and j<n-1)) or (j==n-1 and (i>p and i<n-1)) or (i==n-1 and(j>0 and j<n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

  * * * * * * *   
*
*
*
  * * * * * * *
                *
                *
                *
  * * * * * * *
  """
"""
n=9
p=n//2
for i in range(n):
    for j in range(n):
        if (i==0 or j==p):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

* * * * * * * * * 
        *
        *
        *
        *
        *
        *
        *
        *
"""
"""n=9
p=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and(i>0 and i<n-1)) or (i==n-1 and(j>0 and j<n-1)) or (j==n-1 and(i>0 and i<n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
*               *
*               *
*               *
*               *
*               *
*               *
*               *
  * * * * * * *   """

"""n=10
x=n*2-1
p=n//2
for i in range(n):
    for j in range(x):
        if (i==j or i+j==x-1):
            print("*",end="")
        else:
            print("",end=" ")
    print()

*           *
 *         *
  *       *
   *     *
    *   *
     * *
      *
"""
"""n=5
x=n*2-1
p=n//2
for i in range(n):
    for j in range(x):
        if (j==0)or(i+j==n-1) or(j==x-1) or (j-i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

*       *       * 
*     *   *     *
*   *       *   *
* *           * *
*               *"""
"""
n=5
p=n//2
for i in range(1,n):
    for j in range(n):
        if (j==0)or(i+j==n-1 and i>=p)or(i-j==0 and(i>=p)) or(j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

*       * 
*   *   *
* *   * *
*       *

"""


"""n=9
p=n//2
for i in range(n):
    for j in range(n):
        if (i==j or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

*               * 
  *           *
    *       *
      *   *
        *
      *   *
    *       *
  *           *
*               *
"""
"""n=9
p=n//2
for i in range(1,n):
    for j in range(1,n):
        if (j==p and(i>=p and i<n-1))or(i==j and(i<p)) or(i+j==n-1 and(i<p)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
*           *   
  *       *
    *   *
      *
      *
      *
      *"""

"""
n=10
p=n//2
for i in range(n):
    for j in range(n):
        if (i==0 or i+j==n-1 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

* * * * * * * * * * 
                *
              *
            *
          *
        *
      *
    *
  *
* * * * * * * * * *
"""




