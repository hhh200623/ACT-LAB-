def assign_grade(score):
    if not (0 <= score <= 100):
        print("Invalid score! Enter a value between 0 and 100.")
    else:
        grade = 'FDCBA'[(score >= 60) + (score >= 70) + (score >= 80) + (score >= 90)]
        print(f"Grade: {grade}")
