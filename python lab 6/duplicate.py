#Python program to remove duplicates from Dictionaries
student_data = {'id1': 'Sara','id2': 'David','id3': 'Sara','id4':'Surya'}


result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)
