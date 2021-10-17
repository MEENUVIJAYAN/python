#Python program to reverse a string
a = str(input("Enter the string:"))
for i in range(-1,-len(a)-1,-1):
    print (a[i],end=(" ")) 
