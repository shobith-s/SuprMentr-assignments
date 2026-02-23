students = {
    "Rohan": 85,
    "Sita": 92,
    "Amit": 78,
    "Priya": 95,
    "Vikas": 68
}

topper = max(students, key=students.get)
print(f"Topper: {topper} ({students[topper]} marks)")

average = sum(students.values()) / len(students)
print(f"Class Average: {average:.2f} marks")

print("\nGrades:")
for name, marks in students.items():
    grade = "A" if marks >= 90 else "B" if marks >= 75 else "C" if marks >= 60 else "D"
    print(f"{name}: {marks} -> Grade {grade}")
