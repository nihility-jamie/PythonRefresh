# Enter your height in meters e.g., 1.55
height = 1.75
# Enter your weight in kilograms e.g., 72
weight = 80

bmi = weight / (height ** 2)
if bmi >= 35:
    print(f"Your BMI is {bmi:.4}, you are clinically obese.")
elif bmi >= 30:
    print(f"Your BMI is {bmi:.4}, you are obese.")
elif bmi >= 25:
    print(f"Your BMI is {bmi:.4}, you are slightly overweight.")
elif bmi >= 18.5:
    print(f"Your BMI is {bmi:.4}, you have a normal weight.")
else:
    print(f"Your BMI is {bmi:.4}, you are underweight.")
