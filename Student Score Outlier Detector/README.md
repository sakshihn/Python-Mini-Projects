# 🎓 Student Score Data Cleaner & Analyzer

A simple Python mini project that cleans messy student score data and performs basic analysis.

## 📌 About the Project

This program accepts a comma-separated list of student scores and:

- Cleans invalid values
- Detects outliers (scores greater than 100)
- Creates a cleaned dataset
- Performs basic analysis on valid scores

It is a beginner-friendly project built while learning Python concepts useful for data processing.

## 🚀 Features

- Handles messy user input
- Removes invalid values using exception handling
- Detects and reports outliers
- Generates a cleaned dataset
- Shows simple dataset analytics

## 🧠 Concepts Used

- Python Lists
- Loops (`for`)
- Exception Handling (`try-except`)
- Data Cleaning
- Basic Data Analysis (`len`, `max`, `min`, `sum`)

## 📊 Example Output

```
Enter the Student's score:
32,45,677,23,45,789,132,dfvfv,thnyunm,wqew,34,,hyh745,4,4f

----- Data Cleaning Report -----

Outliers detected: [677, 789, 132]
Invalid values skipped: ['dfvfv', 'thnyunm', 'wqew', '', 'hyh745', '4f']

Cleaned dataset: [32, 45, 23, 45, 34, 4]

----- Dataset Analysis -----

Total number of students: 6
Maximum score: 45
Minimum score: 4
Average score: 30.5
```

## 📂 Project Purpose

This mini project was created as part of a Python learning journey to practice data cleaning and analysis techniques that are useful in data science.

---
