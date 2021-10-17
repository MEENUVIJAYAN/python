#Python program to get a maximum and mininum value in a dictionary
a = {'x':500, 'y':5874, 'z': 560}

maximum = max(a.keys(), key=(lambda k: a[k]))
minimum = min(a.keys(), key=(lambda k: a[k]))

print('Maximum Value: ',a[maximum])
print('Minimum Value: ',a[minimum])
