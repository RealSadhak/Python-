#Simple Arithmetic Operations
friends = 5

friends = friends + 1 
friends += 1

friends = friends - 2 
friends -= 2

friends = friends*5
friends *= 5

friends = friends / 2
friends /= 2

friends = friends**2
friends **= 2

friends = friends%3
friends %= 3

print(friends)


#simple mathematical calculations

x = 3.14
y = 92
z = 838

result = round(x)
result = abs(y)
result = pow(4,5)
result = max(x,y,z)
result = min(x,y,z)
print(result)


# Other Advance mathematical Operations

import math
x = 49.99
print(math.pi) # Value of pie
print(math.e) # Value of e

result = math.sqrt(x) # Square root of a number
result = math.ceil(x) # Always round a number up
result = math.floor(x) # Always round a number down
print(result)


# Exercise 1 - Circumference of a circle

# import math
radius = float (input("Enter the radius of a circle: "))
circumference = 2*math.pi*radius
print(f"The Circumference of the cirle is : {round(circumference,2)}cm")


#Exercise 2 - Area of a circle

# import math
radius = float (input("Enter the radius of a circle: "))
area = math.pi*pow(radius,2)
print(f"The are of the circle is {round(area)}cm^2")


#Exercise 3 - Hypotenuse of the triangle

# import math 
a = float(input("Enter the length of the triangle: "))
b = float(input("Enter the height of the triangle: "))
c = math.sqrt(pow(a,2)+pow(b,2))
print(f"The value of the hypotenuse is {c}cm")