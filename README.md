
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Georgia&weight=600&size=28&duration=2800&pause=900&color=245B8F&center=true&vCenter=true&width=720&lines=Python+Functions+%26+Lists+Assessment;Student+Results+%7C+Class+Performance" alt="Typing SVG" />

# Python Functions and Lists Assessment

**Functions · Strings · Lists · Loops**

[![Language](https://img.shields.io/badge/Language-Python-245B8F?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Assessment](https://img.shields.io/badge/Assessment-2-D58B52?style=for-the-badge)](#)
[![Status](https://img.shields.io/badge/Status-Completed-3C806B?style=for-the-badge)](#)

*A collection of two command-line applications created to practice core Python programming concepts.*

</div>

---

## 1. Project Overview

This repository contains two Python programs developed for the **Functions, Strings and Lists Assessment**.

The programs apply Python concepts to common academic tasks: generating an individual student's result card and analyzing the marks of a class.

The assessment focuses on writing reusable functions, working with strings and lists, validating user input, using loops, and presenting calculated information clearly.

## 2. Applications

### Task 1 — Student Result Card Generator

**File:** `result_card_generator.py`

Generates a formatted result card for one student using marks from five subjects.

**Main features**
- Collects the student's name, roll number, and marks in five subjects.
- Validates the roll number with `isdigit()`.
- Checks that each subject mark is between 0 and 100.
- Cleans and formats the student's name with `strip()` and `title()`.
- Calculates total marks and percentage.
- Assigns a grade from A+ to Fail.
- Sets the final status to Fail if any subject mark is below 40.
- Displays a formatted result card using f-strings.

**Functions used**

| Function | Purpose |
|---|---|
| `format_name(name)` | Removes surrounding spaces and formats the name. |
| `get_valid_marks(subject)` | Requests and validates a subject's marks. |
| `calculate_percentage(total, max_total)` | Calculates the overall percentage. |
| `get_grade(percentage)` | Returns a grade based on the percentage. |
| `get_valid_roll_number()` | Accepts a roll number containing digits only. |

**Grading criteria**

| Percentage | Grade |
|---:|:---:|
| 90 and above | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | Fail |

> **Subject rule:** If a student scores below 40 in any subject, the final status is Fail, regardless of the overall percentage.

### Task 2 — Class Marks Analyzer

**File:** `class_marks_analyzer.py`

Collects student names and marks, then analyzes the academic performance of the class.

**Main features**
- Asks for the number of students.
- Stores names and marks in two separate lists.
- Uses `append()` to add each student's information.
- Validates marks within the range of 0–100.
- Calculates the class average.
- Finds the highest and lowest marks and identifies the students who achieved them.
- Counts passing students (50 or above) and failing students (below 50).
- Displays students who scored above the class average.
- Sorts marks from highest to lowest.
- Displays all student records.

**Custom functions used**

| Function | Purpose |
|---|---|
| `get_student_count()` | Validates the number of students. |
| `get_valid_marks(student_name)` | Requests and validates a student's marks. |
| `calculate_average(student_marks)` | Calculates the class average. |
| `display_highest_lowest(student_names, student_marks)` | Displays highest and lowest marks with student names. |
| `count_pass_fail(student_marks)` | Returns the number of passing and failing students. |

## 3. Python Concepts Used

| Concept | How it is used |
|---|---|
| Functions (`def`) | Divides programs into reusable tasks. |
| Parameters and `return` | Passes information into functions and returns results. |
| String methods | Uses `strip()`, `title()`, and `isdigit()`. |
| Lists | Stores multiple student names and marks. |
| List methods and built-ins | Uses `append()`, `len()`, `sum()`, `max()`, `min()`, and `sorted()`. |
| Loops | Uses `for` and `while` to collect and process information. |
| Conditional statements | Uses `if`, `elif`, and `else` for validation and decisions. |
| Exception handling | Uses `try` and `except` to handle invalid numeric input. |
| F-strings | Displays formatted values and result information. |
| Comments and indentation | Keeps code understandable and properly structured. |
| Dot operator | Accesses methods such as `name.strip()` and `student_names.append()`. |

## 4. Project Structure

```text
python-functions-lists-assessment/
│
├── result_card_generator.py
├── class_marks_analyzer.py
├── demo.html
└── README.md
```

`demo.html` is a visual, browser-based preview of the two Python applications. It presents illustrative sample data; it does not execute or connect to the Python terminal programs.

## 5. Requirements

- Python 3 installed on your computer.
- Visual Studio Code or another Python-supported editor.
- A terminal or command prompt.

No third-party Python packages are required.

## 6. How to Run

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Open the integrated terminal.
4. Run either program separately.

**Run Task 1:**

```bash
py result_card_generator.py
```

**Run Task 2:**

```bash
py class_marks_analyzer.py
```

Follow the prompts in the terminal and enter the requested information.

To view the visual preview, open `demo.html` in a web browser.

## 7. Sample Input and Output

### Task 1 — Student Result Card Generator

**Sample input**

```text
Student Name: Ali Abbas
Roll Number: 12345
English: 95
Mathematics: 90
Computer: 88
Physics: 92
Chemistry: 85
```

**Sample output**

```text
STUDENT RESULT CARD

Student Name       : Ali Abbas
Roll Number        : 12345

SUBJECTS AND MARKS
English            : 95
Mathematics        : 90
Computer           : 88
Physics            : 92
Chemistry          : 85

Total Obtained     : 450 / 500
Percentage         : 90.00%
Grade              : A+
Final Status       : Pass
```

### Task 2 — Class Marks Analyzer

**Sample input**

```text
Number of Students: 5

Ali: 85
Ahmed: 45
Sara: 95
Usman: 60
Ayesha: 75
```

**Sample output**

```text
Highest Marks: 95
Student(s) with Highest Marks:
Sara

Lowest Marks: 45
Student(s) with Lowest Marks:
Ahmed

===== CLASS PERFORMANCE =====
Class Average: 72.00
Passing Students: 4
Failing Students: 1

Students Above Class Average:
Ali: 85
Sara: 95
Ayesha: 75

Marks Sorted (Highest to Lowest):
[95, 85, 75, 60, 45]
```

## 8. Learning Outcomes

By completing this assessment, I practiced:
- Creating and calling functions with parameters and return values.
- Cleaning and validating string input.
- Creating and updating lists.
- Using loops to process multiple student records.
- Applying conditions to grades and class performance.
- Handling invalid input and displaying readable output.

---

<div align="center">

**Developed by Ali Abbas**

*Python Functions and Lists Assessment*

</div>
