"""
problem_5: Given a list, iterate it, and display numbers divisible by five, 
and if you find a number greater than 150, stop the loop iteration.

"""
list_1 = [ 40, 50, 80, 95, 105, 120, 135, 150, 160, 180, 200]

for i in list_1:
    if i < 150:
        if(i % 5 == 0):
            print('This number is divisible by five: ', i)

    else:
       print('Out of range!! Your number is greater than 150')    
       break


    
    
    
  
