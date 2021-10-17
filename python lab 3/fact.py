#Program to print factorial of a number
a = int(input("Enter the number:"))
fact = 1
for i in range(1,a+1):
    fact = fact*i
print(f"Factorial of {a} is {fact}")
