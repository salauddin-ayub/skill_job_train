#d = {}

# key value pair -> key:value
d = {"key1":"value1", 2:10, 3: 10.50}

print(d.keys())
print(d.values())
d2 = {"key2": "value2"}

d.update(d2)
print(d)
#print(d)
#print(d["key1"])

#for i, j in d.items():
    #if i == "key1":
         #print(i, j)

#print(d.get('key1'))  

students = {
    "1234":{
        "name": "Md Jahid Hasan",
        "dept": "SWE"
    },
    "3123":{
        "name": "Md Jawad Hasan",
        "dept": "CSE"
    },
    "3125":{
        "name": "Md Ayub Hasan",
        "dept": "IT"
    }

}

print(students.get("3125"))

student_info = students.get(input())

if student_info == None:
    print("No Data")

else:
    print(student_info['name'], student_info['dept'])    
