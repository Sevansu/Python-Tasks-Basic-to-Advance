#18.Delete an element(key-value pair) from a dictionary.

#here want to delete key 21 and its value
dict1 = {1:{11:111,12:121},2:{21:211,22:221},3:{21:311,22:321}}
print ("")
dictsToRemoveKeysFrom = []
for k,v in dict1.items():
    print (v)
    for i in v.items():
         if (i[0] == 21):
                dictsToRemoveKeysFrom.append(v)

for d in dictsToRemoveKeysFrom:
    d.pop(21)

print(dict1) 