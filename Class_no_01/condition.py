fusong = True

if fusong == True:
    print ("Asle 500 taka treat dewa lgbe")

else:
    print("R noito 1000 taka")    

age = int(input("Enter your age="))


#age= int(age) #type casting

if age >= 18:
    print ("Your age is ok, but do you have nid?") 
    nid = input("Do you have NID? ")
    if nid == True:
        print ("Ok done you can give your vote!!")
    else:
        print ("you don't have your nid, bring it for your vote")  
else:
    print ("You are a teenager, you dont have permission for vote")            