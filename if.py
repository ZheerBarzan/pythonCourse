housePrice =1000000

goodCredit = True

if goodCredit:
    downPayment = 0.1 * housePrice
elif not goodCredit:
    downPayment = 0.2 * housePrice

print (f"Down payment: ${downPayment}")


name = "python"

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good!")