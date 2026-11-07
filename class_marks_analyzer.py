
# Class Marks Analyzer
# This program analyzes the academic performance of a class.


# This function takes a valid positive number of students.
def get_student_count():
    while True:
        try:
            count = int(input("Enter number of students: "))

            if count > 0:
                return count
            else:
                print("Please enter at least 1 student.")

        except ValueError:
            print("Invalid input! Enter a whole number.")


# This function takes valid marks between 0 and 100.
def get_valid_marks(student_name):
    while True:
        try:
            marks = int(input(f"Enter marks for {student_name}: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Please enter numbers only.")


# This function calculates the average marks of the class.
def calculate_average(student_marks):
    return sum(student_marks) / len(student_marks)


# This function displays students with the highest and lowest marks.
def display_highest_lowest(student_names, student_marks):
    highest_marks = max(student_marks)
    lowest_marks = min(student_marks)

    print("\nHighest Marks:", highest_marks)
    print("Student(s) with Highest Marks:")

    for i in range(len(student_marks)):
        if student_marks[i] == highest_marks:
            print(student_names[i])

    print("\nLowest Marks:", lowest_marks)
    print("Student(s) with Lowest Marks:")

    for i in range(len(student_marks)):
        if student_marks[i] == lowest_marks:
            print(student_names[i])


# This function counts passing and failing students.
def count_pass_fail(student_marks):
    passing_students = 0
    failing_students = 0

    for marks in student_marks:
        if marks >= 50:
            passing_students += 1
        else:
            failing_students += 1

    return passing_students, failing_students


# Main program starts here.

print("\n===== CLASS MARKS ANALYZER =====\n")

# Create two separate lists.
student_names = []
student_marks = []

# Get the number of students.
total_students = get_student_count()

# Collect student names and marks.
for i in range(total_students):
    print(f"\nStudent {i + 1}")

    name = input("Enter student name: ").strip().title()

    student_names.append(name)

    marks = get_valid_marks(name)

    student_marks.append(marks)


# Calculate class average.
class_average = calculate_average(student_marks)

# Display highest and lowest marks.
display_highest_lowest(student_names, student_marks)

# Count passing and failing students.
passing_students, failing_students = count_pass_fail(student_marks)


# Display class average.
print("\n===== CLASS PERFORMANCE =====")

print(f"Class Average: {class_average:.2f}")

print(f"Passing Students: {passing_students}")
print(f"Failing Students: {failing_students}")


# Display students scoring above class average.
print("\nStudents Above Class Average:")

found_student = False

for i in range(len(student_marks)):
    if student_marks[i] > class_average:
        print(f"{student_names[i]}: {student_marks[i]}")
        found_student = True

if not found_student:
    print("No students scored above the class average.")


# Sort marks from highest to lowest.
sorted_marks = sorted(student_marks, reverse=True)

print("\nMarks Sorted (Highest to Lowest):")
print(sorted_marks)


# Display all student records.
print("\n===== ALL STUDENT RECORDS =====")

for i in range(len(student_names)):
    print(f"{student_names[i]}: {student_marks[i]}")

print("\n===== ANALYSIS COMPLETED =====")
