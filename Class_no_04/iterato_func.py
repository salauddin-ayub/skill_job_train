for i in range(10):
    print(i, end=" ")

#iteration function
print(range(0, 20, 2))

print('-' * 100)

#iteration vs generator 
def my_range(endpoint):
    for i in range( endpoint):
        yield i

for i in my_range(10):
    print(i, end=" ")     

 # map(func,iter), reduce(func, seq), filter(func, seq)
print('-' * 100)
num = lambda x: x
print(list(map(num, [10, 20, 30, 40, 50])))   


# filter function 
print("--filter--" * 10)

def even_number(number):
    if number % 2 == 0:
        return True
    return False

res = filter(even_number, [1, 3, 4, 7, 8, 10])
print(list(res))