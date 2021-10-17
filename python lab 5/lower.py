#Program to arrange string characters such that lowercase came first
a = str(input("Enter the string:"))
print(sorted(a, key=str.swapcase))
