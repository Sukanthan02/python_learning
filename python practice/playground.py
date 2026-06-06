weight_kg = 93     # weight in kilograms
height_m = 1.83     # height in meters

bmi = weight_kg / (height_m ** 2)
print(f"BMI: {bmi:.2f}")  # .2f → round to 2 decimal places

# Check category using comparison
print(bmi < 18.5)   # Underweight
print(18.5 <= bmi < 24.9)  # Normal weight
print(bmi >= 25.0)  # Overweight