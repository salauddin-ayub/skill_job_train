#list, tuple, set, dictionaries
l = [1, 2, 3.5, 4, 8, 'eight']
print(type(l))

print(l)

#for i in l:
    #print(i)
    #print(type(i))

#indexing
print(l[0])
print(l[3])
print(l[2])



#slicing

print(l[2:5])
print(l[:4])
print(l[-1])
print(l[::-1])

# list mutable Collection

print(l)
l[0] = 1000
print(l)

print(l+[1000])

# built in function
 
l.append(200) 
print(l)

l.reverse()
print(l)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#l.sort
#print(l)

l.pop()
print(l)

p = l.pop()
print(p)
print(l)

print(l.count(200))

# comprehension

l1 = [ i for i in range(10)]
print(l1)

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


  

