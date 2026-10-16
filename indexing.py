credit_card = "123-4567=8901"

print (credit_card[1])
print (credit_card[1:10])
print (credit_card[::])
print(credit_card[0:10:2])

last_digits = credit_card[-4:]
print(f"XXX-XXXX-{last_digits}")