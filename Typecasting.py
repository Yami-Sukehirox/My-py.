# Determining the data type of variables in Python int() boolean() float() str()
full_name = "Lian Cruspero"
age = 11
gpa = 3.75
is_student = True

print (type(full_name))
print (type(age))
print (type(gpa))
print (type(is_student))

#converting data types in Python
gpa = int(gpa)  # Convert float to int
print (gpa)

age = float(age)  # Convert int to float
print (age)

full_name = bool(full_name)  # Convert str to bool
print (full_name)

