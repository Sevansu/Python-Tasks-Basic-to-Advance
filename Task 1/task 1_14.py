#14.Get the numbers which are not divisible by 2 and 3 in the range 2 to 25 using 'filter'.

lst=[*range(2,26)]
print(list(filter(lambda n:n%2 and n%3!=0,lst))) #use of filter & Lambda