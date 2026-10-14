# Input()

full_name = input("What is your name? ")
age = int(input("How old are you? "))

# age = int(age)
age = age + 1


print (f"BELLOO!!, {full_name}!")
print("HAPPY BIRTHDAY!!")
print (f"I'm {age} years old.")

#Area of a rectangle

length = float(input("Enter the length: ")) 
width = float(input("Enter the width: ")) 
area = length * width
print(f"The area of the rectangle is {area}.")

#Shopping Cart

item = input("What item do you want to buy?: ")
price = float(input(f"What is the price?: "))
quantity = int(input(f"How many would you like to buy?: "))

Amount = price * quantity
print(f"The total amount for {quantity} {item}(s) is {Amount}.")