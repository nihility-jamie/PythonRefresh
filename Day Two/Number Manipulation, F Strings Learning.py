print(round(8/3))
print(round(8/3, 2))

# floor division
print((8//3))

result = 4 / 2
result /= 2
print(result)

score = 0
height = 1.8
isWinning = True
print("your score is " + str(score)) # instead of converting to a string for all of them we can use f-string

# f-strings

print(f"your score is {score}")
print(f"your height is {height}m")
print(f"Are you winning? {isWinning}")
print(f"All of them together is, {score, height, isWinning}")
print(f"All of them together is, {score}, {height}, {isWinning}")