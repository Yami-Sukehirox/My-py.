capitals = {"USA": "Washington D.C.",
            "JAPAN": "Tokyo",
            "China": "Beijing",
            "RUSSIA": "Moscow"}

# print(capitals.get("USA"))

# if capitals.get("JAPAN"):
#     print("YES IT EXIST")
# else:
#     print("IT NOT EXIST")


#capitals.update({"Phi": "MAnila"})

# keys = capitals.keys()

# for capital in capitals.keys():    
#     print(capital)

# values = capitals.values()

# for val in capitals.values():
#     print(val)

for key, value in capitals.items():
    print(f"{key}: {value}")