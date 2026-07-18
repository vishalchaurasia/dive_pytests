def calculate_grade(marks):
    """
    Calculate grade based on average marks.

    Rules:
    - marks cannot be empty
    - every mark must be between 0 and 100
    - Average >= 90 : A
    - Average >= 75 : B
    - Average >= 60 : C
    - Otherwise     : F
    """

    if not marks:
        raise ValueError("Marks list cannot be empty.")

    for mark in marks:
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100.")

    average = sum(marks) / len(marks)

    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"



print(calculate_grade([90, 95, 78]))