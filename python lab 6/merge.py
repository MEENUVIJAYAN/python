#python program to merge two dictionaries 
a = {1: 'apple', 2: 'Banana' , 3: 'Orange'}
b = { 4: 'Kiwi', 5: 'Mango'}
print("First Dictionary: ", a)
print("Second Dictionary: ", b)
a.update(b)
    
print("\nAfter Concatenating two Dictionaries : ")
print(a)
