
# Student Result Card Generator
# This program generates a result card for one student.


# This function cleans and formats the student's name.
def format_name(name):
    return name.strip().title()


# This function takes marks and validates them between 0 and 100.
def get_valid_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter {subject} marks: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Please enter numbers only.")


# This function calculates the overall percentage.
def calculate_percentage(total, max_total):
    return (total / max_total) * 100


# This function assigns a grade according to percentage.
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


# This function validates the student's roll number.
def get_valid_roll_number():
    while True:
        roll_number = input("Enter roll number: ").strip()

        if roll_number.isdigit():
            return roll_number
        else:
            print("Invalid roll number! Enter digits only.")


# Main program starts here.

print("\n===== STUDENT RESULT CARD GENERATOR =====\n")

# Get student information.
student_name = format_name(input("Enter student name: "))
roll_number = get_valid_roll_number()

# Store subject names and marks.
subjects = ["English", "Mathematics", "Computer", "Physics", "Chemistry"]
student_marks = {}

# Get marks for all five subjects.
for subject in subjects:
    student_marks[subject] = get_valid_marks(subject)

# Calculate total marks and percentage.
total_obtained = sum(student_marks.values())
max_total = 500

percentage = calculate_percentage(total_obtained, max_total)

# Calculate grade.
grade = get_grade(percentage)

# Check whether any subject has marks below 40.
has_failed_subject = False

for marks in student_marks.values():
    if marks < 40:
        has_failed_subject = True
        break

# Determine final result.
if has_failed_subject:
    final_status = "Fail"
else:
    final_status = "Pass"

# Display the result card.
print("\n" + "=" * 40)
print("          STUDENT RESULT CARD")
print("=" * 40)

print(f"Student Name       : {student_name}")
print(f"Roll Number        : {roll_number}")

print("-" * 40)
print("SUBJECTS AND MARKS")
print("-" * 40)

for subject, marks in student_marks.items():
    print(f"{subject:<20}: {marks}")

print("-" * 40)
print(f"Total Obtained     : {total_obtained} / {max_total}")
print(f"Percentage         : {percentage:.2f}%")
print(f"Grade              : {grade}")
print(f"Final Status       : {final_status}")

print("=" * 40)
print("          RESULT GENERATED SUCCESSFULLY")
print("=" * 40)
