#10.Get the factors of a number given.

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
number=int(input("Enter the number:"))
result=fact(number)
print("Factorial of ",number," is ",result) 