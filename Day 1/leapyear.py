""" leap year program 
year=int(input("Enter a year: "))
if( year%4==0 and year%100!=0 or year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")"""
 
""" print numbers from 1 to 10   
for i in range(1,11):
    print(i)"""


num1=input("Enter first number: ")
num2=input("Enter second number: ")
print("calulation of \n1.sum, \n2.difference, \n3.product and \n4.division of two numbers")
choice=int(input("Enter your choice: "))
if choice==1:
    print(f"sum of {num1} and {num2} is: ",int(num1)+int(num2))
elif choice==2:
    print(f"difference of {num1} and {num2} is: ",int(num1)-int(num2))
elif choice==3:
    print(f"product of {num1} and {num2} is: ",int(num1)*int(num2))
elif choice==4:
    print(f"division of {num1} and {num2} is: ",int(num1)/int(num2))
else:
    print("Invalid choice")

text = input("Enter a string: ")
count = 0
for char in text:
    if char in "aeiouAEIOU":
        count += 1
print(f"The number of vowels in the string is: {count}")