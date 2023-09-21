student_marks = {
    "ash": 95,
    "priya": 24,
    "dev": 34,
    "mikha": 98,
    "anu": 87,
    "ammu": 49,
    "diya": 51
}
a = input("Enter the name: ")
if a in student_marks:
    print(f"Mark : {student_marks[a]}")
else:
    print(f" not found in the dictionary.")
