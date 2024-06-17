num_char = len(input("What is your number?"))

# This will not work as a you cannot concatenate a string with an integer
# print("Your name has " + num_char + " characters.")
print(type(num_char))

#converting the integer to a string.
print("Your name has " + str(num_char) + " characters.")

print(type(float(num_char)))
print(70 + float("100.5"))

