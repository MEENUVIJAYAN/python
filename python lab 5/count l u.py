#Program to count all upper lower and special symbols in a string
a = input("Enter the string:")
l=u=s=n = 0
for i in a:
    if i.islower():
        l+=1
    elif i.isupper():
        u+=1
    elif i.isdigit():
        n+=1
    else:
        s+=1
print("Lower case:",l)
print("Upper case:",u)
print("Digits:",n)
print("Symbols:",s)
