#Python program to remove a key from the dictionaries
a = {'name': 'Meenu', 'age': 20, 'college':'GECB'}
print("Dictionary Items  :  ",  a)

key = input("Enter the key to Delete : ")

if key in a:
    del a[key]
else:
    print("Given Key is Not in this Dictionary")
    
print("Updated Dictionary = ", a)
