"""Collect numbers until 'done', then display a small statistics summary.

Build this program one TODO at a time. The README has the suggested order.
"""


def main():
    # TODO 1: Create your starting values before the loop.
    # Hint: count and total start at 0. What value can smallest/largest use
    # before you've received the first valid number?

    print("Enter numbers one at a time; type 'done' to finish.")

    while True:
        entry = input("Number: ")

        # TODO 2: If entry is "done", leave the loop with break.

        # TODO 3: Convert entry to a number with try/except.
        # If conversion fails, print a friendly message and continue.

        # TODO 4: For a valid number, update count, total, smallest, and
        # largest. Keep these updates inside the loop, but don't reinitialize
        # the running values here.

    # TODO 5: Print count and total. If count is greater than zero, calculate
    # and print the average, smallest, and largest. Otherwise explain that
    # there were no valid numbers to summarize.


if __name__ == "__main__":
    main()
