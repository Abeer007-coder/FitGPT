def get_exercise_plan(goal):
    if goal == "weight_loss":
        return "Cardio + HIIT 5 days/week"
    elif goal == "muscle_gain":
        return "Strength training 4-5 days/week"
    else:
        return "Light exercise + walking"