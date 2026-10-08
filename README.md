# Python Data Analyzer

A beginner Python project that collects numbers, handles invalid input, and reports useful statistics. It grows from the Chapter 5 number analyzer exercise using variables, conditionals, `try`/`except`, loops, counters, accumulators, and functions.

## What it will do

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

## Build it in small steps

Open `number_analyzer.py` and complete one TODO at a time. Run it after each step and try the examples in `examples/sample-session.txt`.

1. Initialize the count, total, smallest, and largest values before the input loop.
2. Ask for input repeatedly and stop when the user types `done`.
3. Convert each other entry to a number inside `try`/`except`. On invalid input, show a message and continue the loop.
4. For a valid number, update the count and total. Update smallest and largest without resetting them each time through the loop.
5. After the loop, print the summary. Only calculate an average when at least one valid number was entered.
6. Optional improvement: move the input-and-summary work into functions once the first version makes sense to you.

## Concepts practiced

Variables · `input()` · strings and numbers · `if`/`else` · `while` · `break` and `continue` · `try`/`except` · counters and accumulators · comparisons · basic functions

## Example result

```text
Enter numbers one at a time; type 'done' to finish.
Number: 10
Number: 5
Number: hello
That wasn't a valid number. Please try again.
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
