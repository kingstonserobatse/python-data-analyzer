# Python Data Analyzer

A beginner Python project that collects numbers, handles invalid input, and reports useful statistics. This learning project was inspired by the number-processing exercises in Chapter 5, “Iteration,” of Python for Everybody: Exploring Data Using Python 3 by Dr. Charles R. Severance. I extended those exercises into an interactive number analyzer that handles invalid input and reports the count, total, average, smallest, and largest values.

## What it does

- Ask for numbers until you type `done`.
- Ignore invalid entries with a helpful message.
- Count accepted numbers and calculate their total and average.
- Find the smallest and largest values.
- Handle the case where no valid numbers were entered.

## Project layout

```text
python-data-analyzer/
├── README.md
├── number_analyzer.py
└── examples/
    └── sample-session.txt
```

## Run it

You need Python 3. Run the program from this folder:

```bash
python number_analyzer.py
```

On some Windows setups, use `py number_analyzer.py` instead.

## How it works

1. Keeps asking for numbers until you type done.

2. Converts each entry to a decimal number. Invalid entries show a message and are skipped.

3. Counts valid numbers, adds them to a running total, and tracks the smallest and largest values.

4. Prints a summary after you type done. If you entered no valid numbers, it explains that there are no statistics to show.

## What I learned

This project gave me practice combining input, loops, conditionals, exception handling, counters, and running totals in one program. I built it step by step and used GitHub commits to record its progress.

## Concepts practiced

Variables · `input()` · strings and numbers · `if`/`else` · `while` · `break` and `continue` · `try`/`except` · counters and accumulators · comparisons · basic functions

## Example result

```text
Enter numbers one at a time; type 'done' to finish.
Number: 10
Number: 5
Number: hello
Error: Invalid input. Please enter numeric values only.
Number: 15
Number: done

--- Results ---
Count: 3
Total: 30.0
Average: 10.0
Smallest: 5.0
Largest: 15.0
```

## Learning note

This repository is a learning project. The starter program intentionally has TODOs: completing and understanding them is part of the project. Add your own explanation, improvements, and Git commit history as you build it.
