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