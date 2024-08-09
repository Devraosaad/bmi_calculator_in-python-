def calculate_bmi(weight , height):
    sum_1= height /100
    bmi=  weight / (sum_1**2)
    return bmi 
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

while True:
 print("Welcome to the BMI Calculator!")
 weight = float(input("Enter the weight  in kg: "))
 height = float(input("Enter the heigth  in centimeter: "))

 bmi = calculate_bmi(weight, height)
 category = categorize_bmi(bmi)
 print(f"Your BMI is: {bmi:.2f}")
 print(f"Your BMI category is: {category}")
 next_calculation = input("Let's do next calculate_bmi ? (yes/no): ")
 if next_calculation.lower() != 'yes':
        break

	
