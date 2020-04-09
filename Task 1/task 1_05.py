'''5. Make a function to get the power of the function. without using the loop. The function should have only two parameters i.e. the number itself and the power. If the power is not passed it should by default take 1. '''

def powe(n,p):
    a=n**p
    return a

num=int(input())
exp=int(input() or '1')
print(pow(num,exp))