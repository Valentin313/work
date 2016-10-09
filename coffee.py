#!/user/etc/env python3

print("What will you be drink: 1-Coffee, 2-Tea, 3-Kakao?")
a =input("Enter the nomber: ")
a =int(a)

if a == 1:
    print("You will be drink 'Coffee'")
    drink = "Coffe"
elif a == 2:
    print("You will be drink 'Tea'")
    drink = "Tea"
elif a == 3:
    print("You will be drink 'Kakao'")
    drink = "Kakao"
else:
    print("You enter not right nomber!")


print("____________ Do you want sugar?__________")
b =input("1-Yes or 2-not?")
b =int(b)
if b == 1:
    print("With sugar")
    sugar = "with sugar"
    c = input('how math?: ')
    sugar = sugar + " " + c
elif b == 2:
    print("Withaut sugar")
    sugar = "withaut sugar"
else:
    print("You enter not right nomber!")

print(drink, sugar)