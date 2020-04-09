'''19.What will the following expressions will return.
    a. x=10, y=23 what will be z if z = x and y
    b. x=1, y='sevansu' what will be z if z = x and y
    c. x=0, y=35, w=False what will be z if z = x and y or w
    d. x=0, y=35 what will be z if z = x and y[0]
    e. x=1 ,y='sevansu' what will be z if z = x and y[0]'''

def a():
    x,y=10,23
    z = x and y
    return z

def b():
    x,y=1,'sevansu'
    z = x and y
    return z

def c():
    x,y,w=0,35,False
    z = x and y or w
    return z

def d():
    x,y=0,35
    z = x and y[0]
    return z

def e():
    x,y=1,'sevansu'
    z = x and y[0]
    return z

print(a())
print(b())
print(c())
print(d())
print(e()) 