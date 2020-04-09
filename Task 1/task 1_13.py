#13.Get Divide by Zero error handled using exception handling in python.

def divide(x, y):
    try:
         result = x / y
    except ZeroDivisionError:
        print("division by zero!(A.K.A Divide by Zero error)")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

num1=int(input("Enter any number:"))
num2=0
divide(num1,num2) 