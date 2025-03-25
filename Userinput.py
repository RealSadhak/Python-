# Input Function = A function that prompts the user to enter data
# Returns the entered data as a string 
# It stores the data as string , so we need to typcasting as per our needs

# f string is used to insert variable in the print statement 
# print(f"This is good !{user_name}")



# input ("What is your name ? ")

user_name = input("What is your name ? ") 
age = int(input("What is your age ? "))  # We can also typecast directly from here !

# age = int(age) {Normal typcasting}

age = age + 1

print(f"Hello! {user_name}")
print(f"You're {age} years old")
print(f"Happy birthday {user_name}")





#Exercise 1 --- Area Calculation

length = float(input("Enter the length : "))
breadth = float(input("Enter the breadth : "))
Area = length*breadth
print(f"Area of the rectangle is {Area}cm^2")




#Exercise 2 --- Shopping Cart Program

item = input("What would you like to buy ? ")
price = float(input("What is the price ? "))
quantity = int(input("How many would you like to have ? "))

Total = price*quantity
print(f"You're are buying {quantity} {item}/s ")
print(f"Your Total is : ${Total}")