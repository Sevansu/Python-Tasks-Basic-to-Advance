#4. {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4} Sort the dictionary and get the result in dictionary itself in 2 lines.

a={'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
sd = sorted(a.items())
for k,v in sd:
    print(k,v)
print("----------------------2nd_Way----------------------")
a={'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
print(sorted(a.items()))