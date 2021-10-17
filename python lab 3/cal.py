print("Please select operation -\n")
select = int(input("Select operations form 1, 2, 3, 4 :")) 
  
a = int(input("Enter first number: ")) 
b= int(input("Enter second number: ")) 
  
if select == 1: 
    print(a, "+", b, "=", 
                   a+b ) 
  
elif select == 2: 
    print(a, "-", b, "=", 
                    a-b) 
  
elif select == 3: 
    print(a, "*", b, "=", 
                    a*b) 
  
elif select == 4: 
    print(a, "/",b, "=", 
                    a/b) 
else:
    print("Invalid input") 
