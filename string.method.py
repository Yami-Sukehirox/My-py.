name = input(("Enter the your full_name: "))
phone_number = input("Enter your PHONE NUMBER #: ")
result = len(name) #find the length (len)
result = name.find("L") #find the string (.find)
result = name.rfind("o") #find the last letter (.rfind)
name = name.capitalize() #This method is making your input name, capital first letter. (.capitalize)
name = name.upper() #This method making the all your input capital. (.upper)
name = name.lower() #This method making your all input lowercase. (.lower)
result = name.isdigit() # This method when all your input is digit it show the digit you input or true
result = name.alpha() #This method if your input is alphabetical it say true without space.

result = phone_number.count("-") #This method count the number of dashes
result = phone_number.replace("-", " ") #This method replace the "-" to spcace " "
print(result)