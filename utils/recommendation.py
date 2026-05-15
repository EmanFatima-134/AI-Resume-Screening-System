# ==========================================
# RECOMMENDATION MODULE
# ==========================================

def generate_recommendation(score):

    if score >= 80:

        return "Excellent Match ⭐"

    elif score >= 65:

        return "Good Match ✅"

    elif score >= 50:

        return "Average Match ⚠️"

    else:

        return "Not Suitable ❌"