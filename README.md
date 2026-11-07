# Python Functions and Lists Assessment

**Student Name:** Ali Abbas  
**Project Name:** Python Functions and Lists Assessment  
**Programming Language:** Python

## 1. Project Overview

This project contains two Python programs developed as part of the Functions, Strings and Lists assessment.

The purpose of this project is to practice Python functions, string manipulation, lists, loops, conditional statements and input validation through simple practical programs.

## 2. Programs Description

### Task 1: Student Result Card Generator

File: `result_card_generator.py`

This program generates a result card for one student.

**Main features:**
- Takes the student's name and roll number as input.
- Takes marks in five different subjects.
- Checks that marks are between 0 and 100.
- Validates the roll number using `isdigit()`.
- Formats the student's name using `strip()` and `title()`.
- Calculates total marks and percentage.
- Assigns a grade according to the given grading criteria.
- Checks whether any subject has marks below 40.
- Displays the final result card with Pass or Fail status.

**Functions used:**

| Function | Purpose |
|---|---|
| `format_name()` | Removes extra spaces and formats the student's name. |
| `get_valid_marks()` | Takes marks and checks their validity. |
| `calculate_percentage()` | Calculates the overall percentage. |
| `get_grade()` | Assigns a grade according to percentage. |
| `get_valid_roll_number()` | Checks that the roll number contains digits only. |

### Task 2: Class Marks Analyzer

File: `class_marks_analyzer.py`

This program analyzes the academic performance of an entire class.

**Main features:**
- Takes the total number of students as input.
- Stores student names and marks in two separate lists.
- Uses `append()` to add student information.
- Validates marks between 0 and 100.
- Calculates the class average.
- Finds the highest and lowest marks.
- Displays the names of students with the highest and lowest marks.
- Counts passing and failing students.
- Displays students who scored above the class average.
- Sorts marks from highest to lowest.

**Custom functions used:**

| Function | Purpose |
|---|---|
| `get_student_count()` | Takes and validates the number of students. |
| `get_valid_marks()` | Takes valid marks for each student. |
| `calculate_average()` | Calculates the class average. |
| `display_highest_lowest()` | Displays highest and lowest marks with student names. |
| `count_pass_fail()` | Counts passing and failing students. |

## 3. Python Concepts and Techniques Used

The following Python concepts are used in both programs:

**1. Functions (`def`)**

Functions are used to divide the program into smaller reusable parts. This makes the code easier to manage and reduces repetition.

**2. Parameters and Return**

Parameters allow functions to receive information, while `return` sends the calculated result back to the part of the program that called the function.

**3. String Manipulation**

- `strip()` removes extra spaces from the beginning and end of a string.
- `title()` makes the first letter of each word capital.
- `isdigit()` checks whether a string contains digits only.

**4. Lists**

Lists are used to store multiple student names and marks.

- `append()` adds new items to a list.
- `len()` returns the number of items.
- `sum()` calculates the total of marks.
- `max()` finds the highest value.
- `min()` finds the lowest value.
- `sorted()` sorts values in ascending or descending order.

**5. Loops**

`for` and `while` loops are used to repeat instructions and process student information.

**6. Conditional Statements**

`if`, `elif` and `else` are used to check conditions, assign grades and determine pass/fail status.

**7. Input Validation and Exception Handling**

`try` and `except` are used to handle invalid numeric inputs and prevent the program from stopping unexpectedly.

**8. F-Strings**

F-strings are used to display variables and calculated results in a readable format.

**9. Comments and Indentation**

Comments explain the purpose of important code sections. Proper indentation maintains the structure of Python code.

**10. Dot Operator (`.`)**

The dot operator is used to access methods associated with an object. For example, `name.strip()` calls the `strip()` method on the name string, while `student_names.append()` calls the `append()` method on a list.

## 4. How to Run the Programs

**Requirements:**
- Python installed on your computer.
- Visual Studio Code or any Python-supported editor.

**Step 1:** Download or clone this repository.

**Step 2:** Open the project folder in Visual Studio Code.

**Step 3:** Open the terminal and run the following commands separately.

To run Task 1:

```bash
py result_card_generator.py
```

To run Task 2:

```bash
py class_marks_analyzer.py
```

Follow the instructions displayed in the terminal and enter the required information.

## 5. Sample Input and Output

### Task 1: Student Result Card Generator

**Sample Input:**

```text
Student Name: Ali Abbas
Roll Number: 12345
English: 95
Mathematics: 90
Computer: 88
Physics: 92
Chemistry: 85
```

**Sample Output:**

```text
STUDENT RESULT CARD

Student Name: Ali Abbas
Roll Number: 12345

English: 95
Mathematics: 90
Computer: 88
Physics: 92
Chemistry: 85

Total Obtained: 450 / 500
Percentage: 90.00%
Grade: A+
Final Status: Pass
```

### Task 2: Class Marks Analyzer

**Sample Input:**

```text
Number of Students: 5

Ali: 85
Ahmed: 45
Sara: 95
Usman: 60
Ayesha: 75
```

**Sample Output:**

```text
Class Average: 72.00

Highest Marks: 95
Student: Sara

Lowest Marks: 45
Student: Ahmed

Passing Students: 4
Failing Students: 1

Students Above Class Average:
Ali: 85
Sara: 95
Ayesha: 75

Marks Sorted:
[95, 85, 75, 60, 45]
```

## 6. Project Structure

```text
python-functions-lists-assessment/
│
├── result_card_generator.py
├── class_marks_analyzer.py
└── README.md
```

## 7. Conclusion

Through this assessment, I practiced Python functions, strings, lists, loops, conditional statements and input validation.

Both programs helped me understand how basic Python concepts can be used to solve practical problems.

**Developed by: Ali Abbas**