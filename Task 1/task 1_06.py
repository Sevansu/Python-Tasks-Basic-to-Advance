'''6.Merge the given two dictionaries in one. {'a': 1, 'c': 3},{'b': 2, 'e': 5, 'd': 4} in one line only. 
'''
d0={'a': 1, 'c': 3}
d1={'a': 1, 'c': 3}
d2={'b': 2, 'e': 5, 'd': 4}
d1.update(d2)
print(d1)
print("------------2nd_Way-------------")
d3={**d0,**d2}
print(d3) 