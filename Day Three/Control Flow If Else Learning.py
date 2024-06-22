print("Welcome To The Rollercoaster")
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age in years: "))
if height >= 120:
    if age >= 18:
        print("Please Pay £10")
    elif age < 18 & age >= 13:
        print("Please Pay £7")
    else:
        print("Please Pay £5")
else:
    print("Sorry, You cannot enter the ride.")