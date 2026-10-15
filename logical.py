# Logical operators

temp = 25
is_raining = False

if temp > 30 or temp < 0 or is_raining:
  print("The event is ekis")
else:
    print("The event is on the goo")    

temp = 25
is_sunny = False

if temp >= 28 and is_sunny:
    print("THE OUTSIDE IS HOT!!")
elif temp <= 0 and is_sunny:
    print("THE OUTSIDE IS COOL")    
elif temp >= 28 and not is_sunny:
    print("It is cloudy")
