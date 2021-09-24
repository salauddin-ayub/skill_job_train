"""
problem_8: Concatenate two lists index-wise
"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_list = [] 
for (item1, item2) in zip(list1, list2):
         sum_list. append(item1+item2)
         print(sum_list) 
