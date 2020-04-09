#2. [1, 'a',3.6000000000000001, 2, 'b', '1', 1.3999999999999999, '2'] sort this list starting with all the numbers sorted and then the characters sorted. The code should be in one line.

def sort(a): 
    a = [str(i) for i in a] 
    a.sort() 
    a = [int(i) if i.isdigit() else i for i in a ] 
    return a 

a = [1,'a',3.6000000000000001,2,'b','1',1.3999999999999999,'2']
print(sort(a))
