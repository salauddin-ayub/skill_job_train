"""
problem_4: Accept number from user and calculate the sum of all number from 1 to a given number

"""

num = int(input("Enter any number: "))
sum = 0

for num in range(1, num+1, 1):
    sum = sum + num
    print("Sum of all number from 1 to your given number: ",sum)