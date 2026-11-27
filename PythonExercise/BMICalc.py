weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI: {bmi:.2f}\n")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
elif 30 <= bmi < 34.9:
    print("You are obese")
else:
    print("You are Extremely obese.")

    