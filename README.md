# Student Grade Analyzer

A simple command-line tool that analyzes a class's grades — built as a Python practice project.

## What It Does

Given a list of students with their names and scores, the program:
- Assigns each student a letter grade (A–F)
- Calculates the class average score
- Identifies the highest and lowest scoring students
- Flags students who are "at risk" (score below 60)
- Reports the overall grade distribution (count per letter grade)

## Example Output

Ana scored 85 with B
Bob scored 45 with F
Cid scored 92 with A
Dan scored 60 with D
Eve scored 73 with C

--- Class Summary ---
Average: 71.0
Highest: Cid (92)
Lowest: Bob (45)
Grade Distribution: {'B': 1, 'F': 1, 'A': 1, 'D': 1, 'C': 1}
At risk: ['Bob']


## How to Run

```bash
python grade_analyzer.py
```

(Requires Python 3.14.1 — no external libraries needed.)

## Skills Practiced

- Functions with return values
- Dictionaries and dictionary comprehensions
- Loops and conditional logic
- Variable scope (local vs. global)

## Possible Improvements

- Accept input from a CSV file instead of hardcoded data
- Handle tie-breaking for highest/lowest scores
- Add input validation for malformed data
