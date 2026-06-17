def calculate_bmi(weight, height_cm):
    print("DEBUG:", weight, height_cm)

    # Strong validation
    if not weight or not height_cm or height_cm <= 0:
        return 0, "Invalid input"

    height_m = height_cm / 100

    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 2), category