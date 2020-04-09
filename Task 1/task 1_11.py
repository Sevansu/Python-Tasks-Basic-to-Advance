#11.Get LCM and GCD of given two numbers

def gcd(x, y):
   while(y):
       gcd_val, y = y, x % y
   return gcd_val

def lcm(x, y):
   lcm_val = (x*y)//gcd(x,y)
   return lcm_val

num1 = int(input('Enter 1st Number:'))
num2 = int(input('Enter 2nd Number:'))

print("The L.C.M. is", lcm(num1, num2))
print("The G.C.D. is", gcd(num1, num2)) 