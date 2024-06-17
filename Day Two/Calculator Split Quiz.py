# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to the Tip Calculator!")
total_bill = input("What is the total bill? \n")
tip_amount = input("What is the tip amount? (10, 12, or 15?) \n")
number_of_people = input("How many people to split the bill? \n")

# I could also just put them before the input.
float_bill = float(total_bill)
int_tip_amount = int(tip_amount)
int_number_of_people = int(number_of_people)

calculated_bill = (float_bill + ((int_tip_amount / 100) * float_bill))
per_person = calculated_bill / int_number_of_people

# Can format to 2 decimal places in different ways.
print(f"Each person should pay: {per_person:.3f}")

per_person = round(per_person, 2)
print(f"Each person should pay: ${per_person}")