#if statements

age = int(input("Enter the age: "))

if age >= 100:
    print("You are too old!")
elif age < 0:
    print("You haven't born yet")
elif age >= 18:
    print("You are an adult")    
else:
    print("You are not an adult")    


food = input("Do you like adobo? (Y/N)")

if food == 'Y':
    print("Same")
elif food == 'N':
    print("ohh sad")
else:
    print("NGEEEE")        