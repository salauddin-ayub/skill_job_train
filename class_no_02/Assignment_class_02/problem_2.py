"""
problem_2:Given a range of the first 10 numbers, Iterate from the start number to the end number, 
and In each iteration
print the sum of the current number and previous number
"""

previous_num = 0

for i in range(10):
    print(i)
    sum = previous_num + i
    print('Current Number is: '+  str(i)  + ' Previous Number : ' + str(previous_num) + ' And sum is : ' +  str(sum) )
    previous_num = i