def analyze_scores(scores):
    total = sum(scores)
    average = round(total / len(scores), 1)
    highest = max(scores)
    lowest = min(scores)

    passed = 0
    for score in scores:
        if score >= 70:
            passed += 1
    
    return {
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed
    }

scores1 = [85, 90, 65, 75, 95]
result1 = analyze_scores(scores1)
print(result1)
