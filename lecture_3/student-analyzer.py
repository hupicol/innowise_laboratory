students = []

def add_student(students):
    name = input("Enter student's name:").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Student '{name}' already exists")
            return
    new_student = {"name": name, "grades": []}
    students.append(new_student)
def add_grades(students):
    if not students:
        print("Please add students first")
        return

    name = input("Enter student's name:").strip()
    student_found = None

    for student in students:
        if student["name"].lower() == name.lower():
            student_found = student
            break

    if not student_found:
        print(f"Student '{name}' not found!")
        return

    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip().lower()
        if grade_input == 'done':
            break
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                student_found["grades"].append(grade)
            else:
                print("Please enter a number between 0 and 100")
        except ValueError:
            print("Please enter a valid number or 'done' to finish")

def calculate_average(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)

def report(students):
    if not students:
        print("No students available")
        return
    print("\n---Student Report---")

    averages = []
    has_grades = False

    for student in students:
        name = student["name"]
        grades = student["grades"]
        try:
            if not grades:
                print(f"{name}'s average grade is N/A")
                continue

            average = calculate_average(grades)
            averages.append(average)
            has_grades = True
            print(f"{name}'s average grade is {average:.2f}")
        except Exception as e:
            print(f"Error showing report {e}")

    if has_grades and averages:
        print("\n------------")
        print(f"Max average: {max(averages):.2f}")
        print(f"Min average: {min(averages):.2f}")
        print(f"Overall average: {sum(averages) / len(averages):.2f}")
    if not has_grades:
        print("\nNo students have grades yet.")


def top_student(students):
    if not students:
        print("No students available")
        return
    students_with_grades = [s for s in students if s["grades"]]

    if not students_with_grades:
        print("No students have grades yet")
        return

    try:
        top_student = max(students_with_grades,
                          key=lambda s: calculate_average(s["grades"]))

        top_average = calculate_average(top_student["grades"])
        print(f"\nThe student with the highest average is {top_student['name']} with a grade of {top_average:.2f}")

    except Exception as e:
        print(f"Error finding top performer {e}")

while True:
    print("--Student Grade Analyzer--")
    print("1.Add a new student")
    print("2.Add a grade for a student")
    print("3.Show report")
    print("4.Find top performer")
    print("5.Exit")
    try:
        choice=input("\nEnter your choice:").strip()
        if choice=="1":
            add_student(students)
        elif choice=="2":
            add_grades(students)
        elif choice=="3":
            report(students)
        elif choice=="4":
            top_student(students)
        elif choice=="5":
            break
        else:
           print("Please enter a number between 1 and 5")
    except Exception as e:
        print(f"An error occurred: {e}")













