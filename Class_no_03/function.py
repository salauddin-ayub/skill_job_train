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
def find_student(id):
    student_info = students.get(id)
    if id == None:
          print("No Student found")

    else:
          print(student_info['name'], student_info['dept'])    

find_student("3125") 

#def getNames(*args, **kwargs):
def get_name(name, name2):
    print(name, name2)

def get_number(*num, **kwargs):
    print(num)
    print(kwargs)

get_number(10, 20, 40, 60, 70, 80, name='Tamim', age='42', dept='CSE')    


get_name("Shiplo", "Halder")

numbers = get_number(10, 20, 30, name='Mash', age='45', dept='CSE')

def mixed_argument(name, age, *args, **kwargs):
    return name+""+str(age)

info = mixed_argument('Sohel', 25)    
print(info)
print(numbers)



