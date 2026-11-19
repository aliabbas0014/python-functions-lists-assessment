 <div align="center">

![Python Functions and Lists](https://capsule-render.vercel.app/api?type=waving&color=0:2563EB,50:7C3AED,100:06B6D4&height=220&section=header&text=Python%20Functions%20%26%20Lists&fontSize=38&fontColor=ffffff&fontAlignY=38&desc=Bootcamp%20Assessment%2002&descAlignY=58&descSize=18)

### Python Bootcamp — Assessment 02

**Two practical Python applications demonstrating Functions, Strings, Lists, Input Validation, and Data Analysis.**

<br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/HTML5-Documentation-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
<img src="https://img.shields.io/badge/GitHub-Pages-222222?style=for-the-badge&logo=githubpages&logoColor=white" alt="GitHub Pages">
<img src="https://img.shields.io/badge/Assessment-02-8B5CF6?style=for-the-badge" alt="Assessment 02">

<br><br>

<a href="https://aliabbas0014.github.io/python-functions-lists-assessment/demo.html">
  <img src="assets/svg-buttons/live-demo.svg" alt="View Live Demo">
</a>
<a href="https://github.com/aliabbas0014/python-functions-lists-assessment">
  <img src="assets/svg-buttons/source-code.svg" alt="View Source Code">
</a>
<a href="#project-documentation">
  <img src="assets/svg-buttons/explore-project.svg" alt="Explore Project">
</a>

</div>

---

## 📌 Project Overview

This repository contains two Python console-based applications developed as part of **Assessment 02** of the Python Bootcamp.

The main purpose of this assessment is to practice Python functions, string manipulation, lists, loops, conditional statements, and input validation through practical programming tasks.

### Applications Included

| Application | Description |
|---|---|
| Student Result Card Generator | Generates a student's result card by calculating total marks, percentage, and grade. |
| Class Marks Analyzer | Analyzes marks of multiple students and displays useful class performance statistics. |

## 🛠️ Technologies & Concepts

- **Language:** Python
- **Documentation & Demo:** HTML5
- **Hosting:** GitHub Pages
- **Functions:** Creating and calling reusable functions
- **Strings:** String formatting and name manipulation
- **Lists:** Storing and processing student marks
- **Loops:** Repeating operations and processing records
- **Conditional Statements:** Applying grading and pass/fail conditions
- **Input Validation:** Handling invalid user input
- **Basic Data Analysis:** Calculating averages, highest marks, and lowest marks

---

# Project Documentation

## 1. Student Result Card Generator

### 📖 Description

The Student Result Card Generator is a Python program that takes a student's information and subject marks as input. It calculates the total marks, percentage, and grade, then displays the result in a properly formatted result card.

The program also applies input validation to ensure that the entered information and marks are within the expected range.

### ⚙️ Main Features

- Takes student name and roll number as input.
- Accepts marks for multiple subjects.
- Validates marks before processing.
- Calculates total obtained marks.
- Calculates overall percentage.
- Assigns a grade according to the percentage.
- Displays the final result card.

### 🧮 Grading Criteria

| Percentage | Grade |
|---|---|
| 90% and above | A+ |
| 80% – 89% | A |
| 70% – 79% | B |
| 60% – 69% | C |
| 50% – 59% | D |
| Below 50% | Fail |

**Passing Condition:** A student must obtain at least 40 marks in each subject to pass the result card assessment.

### 🧩 Function Structure

The program uses separate functions to perform different tasks, making the code easier to understand and maintain.

**Important functions:**
- `format_name()`
- `get_valid_marks()`
- `calculate_percentage()`
- `get_grade()`
- `get_valid_roll_number()`

### 📊 Function Structure Diagram

![Result Card Function Structure](assets/assessment-02/result-card-function-structure.svg)

### 🔄 Result Card Flowchart

![Result Card Flowchart](assets/assessment-02/result-card-flowchart.svg)

### 📋 Result Generation Process

![Result Generation Process](assets/assessment-02/result-generation-process.svg)

### 🎯 Grading Decision Flowchart

![Grading Decision Flowchart](assets/assessment-02/grading-decision-flowchart.svg)

---

## 2. Class Marks Analyzer

### 📖 Description

The Class Marks Analyzer is a Python program designed to process and analyze the marks of multiple students. It stores student marks in lists and performs calculations to provide an overview of class performance.

It helps identify the highest and lowest marks, calculate the class average, and count the number of students who passed or failed.

### ⚙️ Main Features

- Takes marks of multiple students as input.
- Stores marks in a Python list.
- Validates entered marks.
- Calculates the class average.
- Finds the highest and lowest marks.
- Counts passed and failed students.
- Displays a summary of class performance.

### 🧮 Pass/Fail Criteria

| Marks | Status |
|---|---|
| 50 or above | Pass |
| Below 50 | Fail |

### 🧩 Function Structure

The program uses functions to organize the input, processing, and analysis tasks. Lists are used to store and process student marks.

### 📊 Function Structure Diagram

![Class Analyzer Function Structure](assets/assessment-02/class-analyzer-function-structure.svg)

### 🔄 Class Analyzer Flowchart

![Class Analyzer Flowchart](assets/assessment-02/class-analyzer-flowchart.svg)

### 📈 Class Data Processing

![Class Data Processing](assets/assessment-02/class-data-processing.svg)

### 📝 List Processing Workflow

![List Processing Workflow](assets/assessment-02/list-processing-workflow.svg)

---

## 3. Common Project Documentation

This section contains diagrams that explain the overall structure, user interaction, validation, and testing approach used in the project.

### 🏗️ Project Architecture

![Project Architecture](assets/assessment-02/project-architecture.svg)

### 👥 Use Case Diagram

![Use Case Diagram](assets/assessment-02/use-case-diagram.svg)

### ✅ Input Validation Workflow

![Input Validation Workflow](assets/assessment-02/input-validation-workflow.svg)

### 🧪 Test Cases

![Test Cases](assets/assessment-02/test-cases.svg)

### 🔍 Testing Workflow

![Testing Workflow](assets/assessment-02/testing-workflow.svg)

---

## 📁 Project Structure

```text
python-functions-lists-assessment/
│
├── assets/
│   ├── assessment-02/
│   │   ├── project-architecture.svg
│   │   ├── result-card-function-structure.svg
│   │   ├── class-analyzer-function-structure.svg
│   │   ├── use-case-diagram.svg
│   │   ├── result-card-flowchart.svg
│   │   ├── class-analyzer-flowchart.svg
│   │   ├── result-generation-process.svg
│   │   ├── class-data-processing.svg
│   │   ├── grading-decision-flowchart.svg
│   │   ├── input-validation-workflow.svg
│   │   ├── list-processing-workflow.svg
│   │   ├── test-cases.svg
│   │   └── testing-workflow.svg
│   │
│   └── svg-buttons/
│       ├── live-demo.svg
│       ├── source-code.svg
│       └── explore-project.svg
│
├── result_card_generator.py
├── class_marks_analyzer.py
├── demo.html
└── README.md
```

## ▶️ How to Run the Programs

### Requirements

- Python 3.x
- Any code editor (VS Code recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/aliabbas0014/python-functions-lists-assessment.git
```

### Step 2: Open the Project Folder

```bash
cd python-functions-lists-assessment
```

### Step 3: Run Student Result Card Generator

```bash
python result_card_generator.py
```

### Step 4: Run Class Marks Analyzer

```bash
python class_marks_analyzer.py
```

## 🎓 Learning Outcomes

Through this assessment, I practiced and improved my understanding of:

- Creating reusable functions in Python.
- Working with strings and formatting text.
- Using lists to store and manage data.
- Applying loops and conditional statements.
- Validating user input.
- Performing calculations using functions.
- Analyzing student marks and displaying results.
- Organizing programs into smaller and manageable parts.

## 🌐 Live Demo

You can explore the project documentation and interactive demo through the link below.

<div align="center">

<a href="https://aliabbas0014.github.io/python-functions-lists-assessment/demo.html">
  <img src="assets/svg-buttons/live-demo.svg" alt="Explore Live Demo">
</a>

</div>

---

## 👨‍💻 Developer

<div align="center">

<img src="https://img.shields.io/badge/ALI-ABBAS-2563EB?style=for-the-badge&labelColor=111827" alt="Ali Abbas">

### Ali Abbas

**Software Engineering Graduate | Python Bootcamp Student | Web Developer**

Building practical projects while learning and exploring modern technologies.

<br>

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5">
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub">
<img src="https://img.shields.io/badge/GitHub_Pages-222222?style=flat-square&logo=githubpages&logoColor=white" alt="GitHub Pages">

<br><br>

<a href="https://github.com/aliabbas0014">
  <img src="https://img.shields.io/badge/GitHub-View%20Profile-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile">
</a>
<a href="https://www.linkedin.com/in/the-aliabbas/">
  <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
<a href="https://aliabbas0014.github.io/Portfolio/">
  <img src="https://img.shields.io/badge/Portfolio-Visit-7C3AED?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio">
</a>

<br><br>

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2563EB,50:7C3AED,100:06B6D4&height=100&section=footer" width="100%" alt="Footer Banner">

**Python Bootcamp — Assessment 02**

*Learning by building. Improving through practice.*

</div>
