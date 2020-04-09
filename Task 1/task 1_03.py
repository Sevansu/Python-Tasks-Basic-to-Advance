'''3. [1,4,6,7,9,0] Get me the elements from the index as per following. All of the answers should be in one line. 
    a. First three elements
    b. Elements ommitting the first and last elements
    c. Last element
    d. Sort the list in the descending order. '''

a=[1,4,6,7,9,0]
print(a[0:3],end=' ')
print(a[1:5],end=' ')
print(a[0],end=' ')
a.sort(reverse=True)
print(a,end=' ')