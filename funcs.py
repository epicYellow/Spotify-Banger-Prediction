def calculate_impact(coefficients):
    total_impact = sum(abs(value) for value in coefficients.values())
    impact_percentages = {feature: (abs(value) / total_impact) * 100 for feature, value in coefficients.items()}
    return impact_percentages

