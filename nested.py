rows = int(input("Enter the rows: "))
columns = int(input("Enter the comlumns"))
symbol = int(input("Enter the symbol"))

for y in range(rows):
    for x in range(columns):
        print(symbol, end="")
    print()    