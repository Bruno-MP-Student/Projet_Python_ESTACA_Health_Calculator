# src/health_calculator/bmi.py

def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive numbers")
    return round(weight / height**2, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"
