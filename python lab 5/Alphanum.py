#Program to find words with both alphabets and numbers
a = "COVID-19: COVID19 affects different people in different ways. COVID19 infected people will develop mild to moderate illness"
d=l=0
for c in a:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters:", l)
print("Digits:", d)
