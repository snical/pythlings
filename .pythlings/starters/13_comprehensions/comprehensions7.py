# comprehensions7
# Fix the program so it prints `['Ada: 2 passed', 'Mina: 3 passed']`.

# hint: Count scores that are at least 60, and keep both students in the result.
students = [
    {"name": "Ada", "scores": [70, 60, 40]},
    {"name": "Mina", "scores": [100, 80, 60]},
]

reports = [
    student["name"].lower() + ": " + str(sum(score > 60 for score in student["scores"])) + " passed"
    for student in students
    if len(student["scores"]) < 2
]
print(reports)

