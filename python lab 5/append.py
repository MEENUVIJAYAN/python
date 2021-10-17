#Program to append two strings
a = str(input("Enter First String:"))
b = str(input("Enter Second String:"))
l = len(a)
n = ""
m = l//2
n = a[0:m]
n = n+b
n = n + a[m:]
print(n)
