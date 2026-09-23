# Student Performance Tracker 

## Project Overview 

A beginner Python program for recording a student's scores in three subjects, calculating the 
total and average score, assigning a grade, and determining whether the student passed or 
failed. 

## Features
- Collects and validates the student's name
- Accepts decimal scores
- Validates scores between 0 and 100
- Calculates total score
- Calculates average score
- Assigns a grade based on the average
- Determines pass or fail status
- Formats the student's name using title case

## Grade Scale 

Average Score and Grade

70 and above    - A 

60 – 69.99      - B

50 – 59.99      - C 

45 – 49.99      - D

40 – 44.99      - E  

Below 40        - F 

## Python Concepts Used
- Variables
- `input()`
- Type conversion with `float()`
- Strings and string methods
- `.replace()`
- `.isalpha()`
- `.title()`
- `while` loops
- `if`, `elif`, and `else`
- Comparison and logical operators
- f-strings - Basic arithmetic 
- `round()`

## Program Flow 

Get student name   
↓   
Validate student name   
↓   
Get Math score   
↓   
Validate Math score   
↓   
Get English score   
↓   
Validate English score   
↓   
Get Python score   
↓   
Validate Python score   
↓   
Calculate total score   
↓   
Calculate average score   
↓   
Determine grade   
↓   
Display final grade   
↓   
Check Pass/Fail   
↓   
Display result 

## Example 

For a student with: 
- Math: 45.6
- English: 34.0
- Python: 56

The program calculates: 
- Total: 135.6
- Average: 45.2 
- Grade: D
- Status: Passed

## Challenges 

One challenge was validating names containing spaces. Since `.isalpha()` returns `False` when  a 
string contains spaces, `.replace(" ", "")` was used before checking whether the remaining 
characters were alphabetic. 

Another challenge was ensuring that scores outside the 0–100 range were rejected and the 
user was asked to enter the score again. 

## What I Learned 

This project helped me practise input validation, loops, conditional statements, string methods, 
type conversion, calculations, and basic program flow. 

It also helped me understand how different Python concepts can work together to create a 
complete program. 

## Future Improvements

- Add error handling for non-numeric score inputs
- Allow the program to process multiple students
- Store student records
- Improve the output formatting

## Project Status

Completed beginner Python project.
