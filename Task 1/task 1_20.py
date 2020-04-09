#20. Multiply two lists' element in one. [1,2,3,4,5][6,7,8,9,10] the result should be [6,14,24,36,50].


list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3 = [] 
for i in range(0, len(list1)): 
    list3.append(list1[i] * list2[i]) 
print(list1)
print(list2)
print(list3) 