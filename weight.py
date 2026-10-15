#Weight converter 

converter = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if converter == "K":
    converter = converter * 2.205
    unit = "Lbs."
elif converter == "L":
    converter = converter / 2.205
    unit = "kgs."
else:
    print(f"{unit} the choice is not valid!")    

print(f"Your weight is {converter} {unit}")