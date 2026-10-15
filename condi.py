#conditional expression

num = 4
a = 6
b = 7
age = 25
temp = 40
user_role = "admin"

#print("POSITIVE" if num > 0 else "NEGATIVE")
#result = "EVEN" if num % 2 == 0 else "ODD"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Adult" if age >= 18 else "MINOR"
#weather = "HOT" if temp > 25 else "COLD"
access_level = "Full Access" if user_role == "admin" else "NOT ADMIN"

print(access_level)