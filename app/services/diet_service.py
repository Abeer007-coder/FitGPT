def get_diet_plan(disease):
    if disease == "diabetes":
        return "Low sugar, high fiber diet. Avoid refined carbs."
    elif disease == "bp":
        return "Low sodium diet. Avoid processed foods."
    else:
        return "Balanced diet with carbs, protein, and healthy fats."