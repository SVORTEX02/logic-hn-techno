#n=int(input("Enter Number:"))
"""for i in range(0,n):
    for j in range(n-i):
        print("*",end=" ")
    print()
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*"""

"""for i in range(0,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end=" ")
    print()

     * 
    * *
   * * *
  * * * *
 * * * * *
* * * * * *"""
"""n=8
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,n-i):
        print("*",end=" ")
    print()

* * * * * * * * 
 * * * * * * *
  * * * * * *
   * * * * *
    * * * *
     * * *
      * *
       *"""
"""n=5
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(0,i):
        print("*",end=" ")
    print()
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,n-i):
        print("*",end=" ")
    print()
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *"""
"""n=7
for i in range(0,n+1):
    for j in range(0,n-i):
        print("",end="  ")
    for k in range(0,i+1):
        print(" *",end="")
    print()

               *
             * *
           * * *
         * * * *
       * * * * *
     * * * * * *
   * * * * * * *
 * * * * * * * *"""


"""n=10
for i in range(0,n+1):
    for j in range(0,n-i,):
        print("*",end="")
    for k in range(0,i):
        print("  ",end="")
    for l in range(n-i):
        print("*",end="")
    print()

********************
*********  *********
********    ********
*******      *******
******        ******
*****          *****
****            ****
***              ***
**                **
*                  *
   
"""

"""n=10
for i in range(0,n+1):
    for j in range(0,i+1):
        print("*",end="")
    for k in range(0,n-i):
        print(" ",end=" ")
    for l in range(0,i+1):
        print("*",end="")
    print()
*                    *
**                  **
***                ***
****              ****
*****            *****
******          ******
*******        *******
********      ********
*********    *********
**********  **********
**********************"""
"""
n=10
for i in range(1,n+1):
    for j in range(1,n+1,1):
        if(i==1 or i==n or j==1 or j==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

* * * * * * * * * * 
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
* * * * * * * * * *"""
         
"""n=int(input("enter number"))
x=n*2-1
p=x//2

for i in range(0,n+1):
    for j in range(x):
        if(j==0 or i==0 or j==x-1 or j-i==p-1 or j+i==p+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
 
    print()

* * * * * * * * *
*       *       *
*     *   *     *
*   *       *   *
* *           * *
*               *"""

"""n=10
for i in range(n):
    for j in range(n):
        if(j==0 or i==0 or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
* * * * * * * * * * 
*               *
*             *
*           *
*         *
*       *
*     *
*   *
* *
*"""
"""n=10
for i in range(n):
    for j in range(n-i):
            print("*",end=" ")
    print()
* * * * * * * * * * 
* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*"""


"""n=5
x=n*2-1
p=n//2
for i in range(n):
    for j in range(x):
        if (j==0 or i==j or j==x-1 or i+j==x-1 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

*               * 
* *           * *
*   *       *   *
*     *   *     *
* * * * * * * * *"""




