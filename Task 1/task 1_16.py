#16.Convert a string to a list. 'sevansu' ==> ['s','e','v','a','n','s','u']

string1 = 'sevansu'

# f-strings way
print(f'List of Characters ={list(string1.strip())}')

# old ways
print('List of Characters = {0}'.format(list(string1.strip()))) 