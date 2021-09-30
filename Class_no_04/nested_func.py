def first_func():
    def sec_func():
        print("This is an inner function")
    sec_func()
    print("This is an outer function")

def outter_func(name):
    def inner_func():
        print("welcome ", name)   
    return inner_func() 

def factorial(number):
    try:
        if not isinstance(number, int):
           raise TypeError("Sorry, number must be an integer")   
        if number < 0:
           raise ValueError("Please input number must be bigger than 0")   

        def cal_fact(num):
           if num <= 1:
               return 1
           return num*cal_fact(num-1)

        return cal_fact(number) 
    except Exception as e:
        print(e)    

    

print(factorial(5))                    

first_func()
outter_func("jahid")    



# lambda function 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
