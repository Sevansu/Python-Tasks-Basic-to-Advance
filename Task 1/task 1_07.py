'''7.Merge two lists using the function of list and sort the resultant list in reverse order. [1,3,5,7,9],[2,4,6,8,10]'''

l1=[1,3,5,7,9]
l2=[2,4,6,8,10]
l3=[*l1,*l2]
l3.sort(reverse=True)
print(l3) 