def calculate_calories(age, gender, weight, height, activity_level, goal):
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_map = {
        "low": 1.2,
        "moderate": 1.55,
        "high": 1.725
    }

    tdee = bmr * activity_map.get(activity_level, 1.2)

    if goal == "weight_loss":
        calories = tdee - 500
    elif goal == "muscle_gain":
        calories = tdee + 300
    else:
        calories = tdee

    return round(calories, 2)