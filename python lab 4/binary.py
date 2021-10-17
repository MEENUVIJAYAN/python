#Program to read a number and print the binary of that number
n = int(input("Enter a number: "))
a = ""
while n > 0 :
    a = str(n % 2) + a
    n = int(n / 2)
print("Binary number :", a)
