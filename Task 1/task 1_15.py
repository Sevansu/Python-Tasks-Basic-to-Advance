#15.Get the following result using numbers 1 to 10 (Use Range) as input and without using multiplication or if condition. [2,4,6,8,10,12,14,16,18,20]

lst1=[*range(1,11)]
double=list(map(lambda n:n*2,lst1))#Use of Map Function
print(double) 