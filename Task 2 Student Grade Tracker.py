#TASK TWO:STUDENT GRADE TRACKER
total_grades = 0
subject_count = 0

while True:
    c = int(input("Enter a Subject No.: "))
    a = input("Enter a Subject Name: ")
    g = int(input(f"Enter a grade for {a} (0-100): "))

    if g > 100 or g < 0:
        print("Entered wrong Grade. Please enter a value between 0 and 100.")
        continue

    total_grades += g
    subject_count += 1
    print(f"Subject {a} Grade is: {g}")
    if g >= 95:
        print("Grade: O")
    elif g >= 90:
        print("Grade: A+")
    elif g >= 80:
        print("Grade: A")
    elif g >= 70:
        print("Grade: B+")
    elif g >= 60:
        print("Grade: B")
    elif g >= 50:
        print("Grade: C+")
    elif g >= 40:
        print("Grade: C")
    elif g >= 35:
        print("Grade: D")
    else:
        print("Grade: U / Failed")
    m = input("Do you want to add another subject? (yes/no): ").strip().lower()
    if m != "yes":
        break

if subject_count > 0:
    average_grade = total_grades / subject_count
    print(f"\nAverage Grade: {average_grade:.2f}")

    if average_grade >= 95:
         overall_grade = "O"
    elif average_grade >= 90:
        overall_grade = "A+"
    elif average_grade >= 80:
        overall_grade = "A"
    elif average_grade >= 70:
        overall_grade = "B+"
    elif average_grade >= 60:
        overall_grade = "B"
    elif average_grade >= 50:
        overall_grade = "C+"
    elif average_grade >= 40:
        overall_grade = "C"
    elif average_grade >= 35:
        overall_grade = "D"
    else:
        overall_grade = "U / Failed"

    print(f"Overall Grade: {overall_grade}")

    gpa =average_grade/10

    print(f"GPA (10.00scale): {gpa:.2f}")
else:
    print("No grades entered to calculate an average.")