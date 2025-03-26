# if = do some code only IF some condition is True 
#                        Else do something else


#Example 1
age = int(input("Enter your age: "))

if age >=60:
    print("You are eligible to vote and You are a senior citizen !")

elif age >= 18:
    print("You are eligible to vote !")

elif age<0:
    print("You have not  born yet !")
else:
    print("You must be 18+ for the eligibility of vote !")



#Example 2
name = input("Enter your name : ")

if name == "":
    print("You did not type in your name !")
else:
    print(f"Thank you {name} 17!")



#Example 3

for_sale = False

if for_sale:
    print("This car is for sale !!")
else:
    print("This car is NOT for sale !!")


#Example 4

online = True 

if online:
    print("The user is online !")
else:
    print("The user is offline !")