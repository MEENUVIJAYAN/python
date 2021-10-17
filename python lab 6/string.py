#Python program to create a dictionary from a string
from collections import defaultdict, Counter
str1 = 'w3resource' 
a = {}
for letter in str1:
    a[letter] = a.get(letter, 0) + 1
print(a)
