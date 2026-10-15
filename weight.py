#Weight converter 

converter = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    converter = converter * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(converter, 2)} {unit}")
elif unit == "L":
    converter = converter / 2.205
    unit = "Kgs."
    print(f"Your weight is {round(converter, 2)} {unit}")
else:
    print(f"{unit} choice is not valid!")    

