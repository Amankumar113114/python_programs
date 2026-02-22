# Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if(b==0):
        print("not defined")
    else:
        return a/b
    
print("select operator")
print("1.addition")
print("2.subtraction")
print("3.multiply")
print("4.divide")
while True:
 opt=int(input("enter operator number :"))
 if opt in (1,2,3,4):
   try:
    num1=float(input("enter first number :"))
    num2=float(input("enter second number :"))
   except:
    print("invalid input please enter a number  between(1 to 4)")
    continue
   if(opt==1):
    print(add(num1,num2))
   elif(opt==2):
    print(sub(num1,num2))
   elif(opt==3):
    print(multiply(num1,num2))
   elif(opt==4):
    print(divide(num1,num2))
    next_cal=input(" you want next calculation (yes/no)")
   if next_cal=="no":
    break
 else:
   print("invalid input")

