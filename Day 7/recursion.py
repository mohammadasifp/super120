#WAP a python program to print numbers from 1 to n using recursion
"""
def printN(n):
    if n>0:
        printN(n-1)
        print(n)
        
printN(5)
"""
#WAP a python program to print numbers from n to 1 using recursion
'''
def printNto1(n):
    if n>0:
        print(n)
        printNto1(n-1)
printNto1(5)      
'''
#WAP a python program to find sum of n numbers using recursion
'''
def sumofN(n):
    if n==0:
        return 0
    else:
        return n+sumofN(n-1)
    
sum=sumofN(5)
print("sum of n numbers is :",sum)
'''

# wap a python program to find factorial of a number using recursion
'''
def fact(n):
    if n==0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

n=int(input("Enter the n value :"))
fact1=fact(n)
print(f"factorial of {n} is :{fact1}")

'''
# wap a python program to find fibonacci series of n numbers using recursion
'''
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=int(input("Enter the n value :"))
fib1=fib(n)
print(f"fibonacci series of {n} is :{fib1}")
'''
# wap a python program to find power of a number using recursion
'''
def powerN(m,n):
    if n==1:
        return m
    else:
        return m*powerN(m,n-1)
m=int(input("Enter the base value :"))
n=int(input("Enter the exponetial value :"))
power=powerN(m,n)
print(f"base value {m} and exponetial value {n} :power is {power}")
'''
# wap a python program to count number of digits in a number using recursion
'''
def countofDigit(n):
    if n==0:
        return 0
    else:
        return 1+countofDigit(n//10)

n=int(input("Enter the n value :"))
countis=countofDigit(n)
print(f"count of digits {n} is :{countis}")  
'''

#power set 
a=[]
n=int(input("Enter the n value :"))
for i in range(n):
    a.append(int(input("Enter the value :")))
print("[",end="")
for i in range(n):
    print(a[i],end="")
print("]")
def subset(a,n):
    if n==0:
        return [[]]
    else:
        sub=subset(a,n-1)
        x=a[n-1]
        newsubset=[]
        for i in sub:
            newsubset.append(i)
            newsubset.append(i+[x])
        return newsubset