def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    if num1==0 or num2==0:
        return "division by zero is not possible"
    return num1/num2

def mod(num1,num2):
    if num1==0 or num2==0:
        return "division by zero is not possible"
    return num1%num2
     

print("|-----    CALCULATOR         -----|")
print("|-----    1.ADDITION         -----|")
print("|-----    2.SUBTRACTION      -----|")
print("|-----    3.MULTIPLICATION   -----|")
print("|-----    4.DIVISION         -----|")
print("|-----    5.MODULUS          -----|")
print("|-----    6.EXIT             -----|")

run=True
while(run):
    choice=input("enter your choice:")
    if choice not in ["1","2","3","4","5","6"]:
        print("X--     INVALID CHOICE     --X")
        continue
    num1=int(input("enter the first number  :"))
    num2=int(input("enter the second number :"))
    if choice=="1":
        print("RESULT :",add(num1,num2))
    elif choice=="2":
        print("RESULT :",subtract(num1,num2))
    elif choice=="3":
        print("RESULT :",multiplication(num1,num2))
    elif choice=="4":
        print("RESULT :",division(num1,num2))
    elif choice=="5":
        print("RESULT :",mod(num1,num2))
    elif choice=="6":
        print("|     THANKS FOR USING OUR CALCULATOR      |")
        run=False
    print("-"*35)
        
     
    



