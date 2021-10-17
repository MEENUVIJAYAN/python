#Program to read the range and dispaly the numbers that is divisible by 3 and 5
a = int(input("Enter lower range limit:"))
b = int(input("Enter upper range limit:"))
for i in range(a, b+1):
   if((i%3==0) & (i%5==0)):
      print(i)
