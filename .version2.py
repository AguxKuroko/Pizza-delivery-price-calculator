print( "Welcome to Pizza Delivery!")
size = input("What size of pizza do you want? S , M , L?")
pepperoni = input("Do you want pepperoni? Y, N ?")
extra_cheese = input("Do you want extrea cheese ? Y, N ?")

bill = 0

if size == "S":
    bill+= 15
elif size == "M":
    bill+= 20
else:
    bill+= 25

if pepperoni == "Y":
    if size == "S":
        bill+= 2
    else:
        bill+= 3

if extra_cheese == "Y":
    bill+= 1

print(f"Your totall bill: {bill}. Thank you and visit us again!")
