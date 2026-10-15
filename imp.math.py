#import math

#x = 10
#print(math.pi)
#print(math.e)
#result = math.sqrt(x) #sqrt function returns the square root of a number
#result = math.ceil(x) #ceil function returns the smallest integer greater than or equal to a number
#print = math.floor(x) #floor function returns the largest integer less than or equal to a number
#print(result)

import math

#radius = float(input("Enter the radius of circle: "))

#circumference = 2 * math.pi * radius

#print (f"The Circumference of a Circle is {round(circumference, 2)}cm")

radius = float(input(f"Enter the radius of circle: "))

area = math.pi * pow (radius, 2)

print (f"The Area of a Circe is {round(area, 2)}cm^2")
