#Program to check the triangle is equilateral or not.

print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
else:
    print("Not equilateral triangle")
